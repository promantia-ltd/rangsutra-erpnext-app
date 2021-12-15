from __future__ import unicode_literals
import frappe, erpnext
from frappe import _
import json
import re
from erpnext.controllers.stock_controller import StockController
import datetime

class StockEntry(StockController):
    pass

@frappe.whitelist()
def generate_ewaybill_json(dt,dn):
    ewaybills = []
    doc = frappe.get_doc(dt, dn)
    s_warehouse = doc.items[0].s_warehouse
    t_warehouse = doc.items[0].t_warehouse
    from_address =''
    from_address2 =''
    to_address = ''
    to_address2 = ''
    gstin =''
    trans_doc_no = doc.transport_receipt_no
    mode_of_transport = doc.mode_of_transport
    distance = doc.distance
    vehicle_no = ''
    if doc.vehicle_no:
        vehicle_no = doc.vehicle_no.replace(' ', '')
    if s_warehouse:
        s_address = frappe.db.sql("""select
                distinct `tabAddress`.gstin, `tabAddress`.address_line1,`tabAddress`.address_line2,
                `tabAddress`.city,`tabAddress`.gst_state_number,`tabAddress`.pincode
            from
                `tabAddress`, `tabDynamic Link`
            where
                `tabDynamic Link`.parent = `tabAddress`.name and
                `tabDynamic Link`.parenttype = 'Address' and
                `tabDynamic Link`.link_doctype = 'Warehouse' and
                `tabAddress`.is_primary_address =  1 and
                `tabDynamic Link`.link_name = %(warehouse)s""", {"warehouse": s_warehouse})
        if len(s_address) > 0:
            from_address = s_address[0][1]
            gstin = s_address[0][0]
            from_address2 = s_address[0][2]
            from_state_code = s_address[0][4]
            from_pincode = s_address[0][5]
            from_city = s_address[0][3]


    if t_warehouse:
        t_address = frappe.db.sql("""select
                distinct `tabAddress`.gstin, `tabAddress`.address_line1,`tabAddress`.address_line2,
                `tabAddress`.city,`tabAddress`.gst_state_number,`tabAddress`.pincode
            from
                `tabAddress`, `tabDynamic Link`
            where
                `tabDynamic Link`.parent = `tabAddress`.name and
                `tabDynamic Link`.parenttype = 'Address' and
                `tabDynamic Link`.link_doctype = 'Warehouse' and
                `tabAddress`.is_primary_address =  1 and
                `tabDynamic Link`.link_name = %(warehouse)s""", {"warehouse": t_warehouse})
        
        if len(t_address) > 0:
            to_address = t_address[0][1]
            to_address2 = t_address[0][2]
            to_state_code = t_address[0][4]
            to_pincode = t_address[0][5]
            to_city = t_address[0][3]

    igst = 0
    cgst = 0
    sgst = 0
    total_tax_amount = 0
    if doc.taxes:
        for row in doc.taxes:
            if 'IGST' in row.account_head:
                igst += row.tax_amount
            if 'CGST' in row.account_head:
                cgst += row.tax_amount
            if 'SGST' in row.account_head:
                sgst += row.tax_amount
            total_tax_amount += row.tax_amount

    fields = ["source_warehouse","target_warehouse","gstin", "from_address", "to_address",
		"mode_of_transport","transport_receipt_no"]
    field_values = [s_warehouse,t_warehouse,gstin, from_address, to_address,
		mode_of_transport,trans_doc_no]
        
    reqd_fields =  dict(zip(fields, field_values))
    for fieldname,values in reqd_fields.items():
        if values == '' or values == None:
            frappe.throw(_('{} is required to generate E-Way Bill JSON').format(fieldname))


    transport_modes = {
		'Road': 1,
		'Rail': 2,
		'Air': 3,
		'Ship': 4
	}

    if doc.mode_of_transport == 'Road':
        if not doc.gst_transporter_id and not doc.vehicle_no:
            frappe.throw(_('Either GST Transporter ID or Vehicle No is required if Mode of Transport is Road'))
        if not doc.gst_vehicle_type:
            frappe.throw(_('Vehicle Type is required if Mode of Transport is Road'))

    vehicle_types = {
		'Regular': 'R',
		'Over Dimensional Cargo (ODC)': 'O'
	}
    
    data = frappe._dict({
            "OthValue": 0,
            "TotNonAdvolVal": 0
		})
    data.actualFromStateCode = from_state_code
    data.actualToStateCode = to_state_code
    data.cessValue = 0
    data.cgstValue = 0 if cgst == 0 else "{:.2f}".format(cgst)
    data.docDate = datetime.datetime.strptime(str(doc.posting_date), "%Y-%m-%d").strftime("%d/%m/%Y")
    data.docNo = doc.name
    data.docType = "INV"
    data.fromAddr1 = from_address
    data.fromAddr2 = from_address2
    data.fromGstin = gstin
    data.fromPincode = from_pincode
    data.fromPlace = from_city
    data.fromStateCode = from_state_code
    data.fromTrdName = s_warehouse
    data.igstValue = 0 if igst == 0 else "{:.2f}".format(igst)
    data.itemList = []
    data = get_item_list(data, doc)#itemList.append(item_data)
    data.sgstValue = 0 if sgst == 0 else "{:.2f}".format(sgst) 
    data.subSupplyType = 1
    data.supplyType = "O"
    data.toAddr1 = to_address
    data.toAddr2 = to_address2
    data.toGstin = "URP"
    data.toPincode = to_pincode
    data.toPlace = to_city
    data.toStateCode = to_state_code
    data.toTrdName = t_warehouse
    data.totInvValue = doc.net_total+total_tax_amount
    data.totalValue = doc.total
    data.transDistance = distance
    data.transDocDate = datetime.datetime.strptime(str(doc.transport_receipt_date), "%Y-%m-%d").strftime("%d/%m/%Y")
    data.transDocNo = trans_doc_no
    data.transMode = transport_modes.get(doc.mode_of_transport)
    data.transType = 1
    data.transporterId = doc.gst_transporter_id or ""
    data.transporterName = doc.transporter_name or ""
    data.userGstin = gstin
    data.vehicleNo = vehicle_no
    data.vehicleType = vehicle_types.get(doc.gst_vehicle_type) or ""
    ewaybills.append(data)
    data = {
		'version': '1.0.0421',
		'billLists': ewaybills
	}
    return data



def get_item_list(data, doc):
    sgst = 0
    cgst = 0
    igst = 0
    total_inclusicve_rate = 0
    if doc.taxes:
        for row in doc.taxes:
            if 'IGST' in row.account_head:
                igst += row.rate
            if 'CGST' in row.account_head:
                cgst += row.rate
            if 'SGST' in row.account_head:
                sgst += row.rate
            if row.included_in_print_rate == 1:
                total_inclusicve_rate += row.rate


    for items in doc.items:
        hsn_code = frappe.db.get_value("Item",{'name':items.item_code},'gst_hsn_code')
        if not hsn_code:
            frappe.throw(_('GST HSN Code does not exist for one or more items'))
        item_data = frappe._dict()
        item_data.cessNonAdvol = 0
        item_data.cessRate = 0
        item_data.cgstRate = cgst
        item_data.hsnCode = int(hsn_code)
        item_data.igstRate = igst
        item_data.qtyUnit = ""
        item_data.sgstRate = sgst
        taxable_amt = 0
        if total_inclusicve_rate > 0:
            taxable_amt = (items.amount - ((items.amount * total_inclusicve_rate)/(100+total_inclusicve_rate)))
        else:
            taxable_amt = row.amount
        item_data.taxableAmount = taxable_amt
    
        data.itemList.append(item_data)

    return data