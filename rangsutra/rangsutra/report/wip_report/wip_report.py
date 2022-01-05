# Copyright (c) 2013, rangsutra_app and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _

def execute(filters=None):
	data = []
	columns = get_columns()
	conditions = get_conditions(filters)
	data.extend(get_inhouse_data(filters,conditions))
	data.extend(get_subcontract_data(filters,conditions))
	return columns, data

def get_columns():
	columns = [
		{
			"fieldname": "blanket_order",
			"label": _("Blanket Order"),
			"fieldtype": "Link",
			"options": "Blanket Order",
			"width": 200
		},
		{
			"fieldname": "style",
			"label": _("Style"),
			"fieldtype": "Link",
			"options": "Item",
			"width": 200
		},
		{
			"fieldname": "work_order",
			"label": _("Work Order / PO"),
			"fieldtype": "Dynamic Link",
			"options" : "doctype",
			"width": 200
		},
		{
			"fieldname": "process",
			"label": _("Process"),
			"fieldtype": "data",
			"width": 200
		},
		{
			"fieldname": "workstation",
			"label": _("Workstation"),
			"fieldtype": "data",
			"width": 200
		},
		{
			"fieldname": "issue_qty",
			"label": _("Issue Qty"),
			"fieldtype": "Float",
			"width": 200
		},
		{
			"fieldname": "receive_qty",
			"label": _("Receive Qty"),
			"fieldtype": "Float",
			"width": 200
		},
		{
			"fieldname": "balance_qty",
			"label": _("Balance Qty"),
			"fieldtype": "Float",
			"width": 200
		},
		{
			"fieldname": "reject_qty",
			"label": _("Rejected Qty"),
			"fieldtype": "Float",
			"width": 200
		},
		{
			"fieldname": "returned_qty",
			"label": _("Return without jobwork"),
			"fieldtype": "float",
			"width": 200
		}
	]
	return columns

def get_inhouse_data(filters,conditions):
	#returns work_order, blanket_order details form production plan
	query="""SELECT t1.production_plan, t1.blanket_order, t1.work_order, t1.doctype, t1.style, t1.process, t1.workstation,
		COALESCE(t1.issue_qty,0) as "issue_qty", COALESCE(t1.receive_qty,0) as "receive_qty", COALESCE((t1.issue_qty-t1.receive_qty),0) as "balance_qty",
		COALESCE(t1.reject_qty, 0) as "reject_qty", COALESCE(t1.returned_qty,0) as "returned_qty" from
		(SELECT DISTINCT
		pp.name as "production_plan",
		(CASE WHEN pp.get_items_from = 'Sales Order' THEN soi.blanket_order ELSE mri.blanket_order END) as "blanket_order",
		wo.name as "work_order",
		"Work Order" as doctype,
		(CASE WHEN pp.get_items_from = 'Sales Order' THEN (SELECT i.variant_of from `tabItem` i where i.name = soi.item_code)
		ELSE (SELECT mi.variant_of from `tabItem` mi where mi.name = mri.item_code)END) as "style",
		woo.operation as "process",
		woo.workstation ,
		(SELECT SUM(woi.transferred_qty) from `tabWork Order Item` woi inner join `tabItem` fti on woi.item_code = fti.name
		where woi.parent = wo.name and (fti.fabric_or_yarn = 1 or fti.intermediate_product = 1) GROUP BY woi.parent) as "issue_qty",
		wo.produced_qty as "receive_qty",
		(SELECT sum(se.fg_completed_qty) from `tabStock Entry` se where se.work_order = wo.name and se.stock_entry_type = 'Manufacturing Reject') as "reject_qty",
		(SELECT sum(se.fg_completed_qty) from `tabStock Entry` se where se.work_order = wo.name and se.stock_entry_type = 'Manufacturing Return') as "returned_qty"
		from `tabProduction Plan` pp 
		LEFT join `tabProduction Plan Sales Order` ppso
		on pp.name = ppso.parent and pp.get_items_from = 'Sales Order'
		LEFT join `tabSales Order Item` soi
		on ppso.sales_order = soi.parent 
		inner join `tabWork Order` wo
		on pp.name = wo.production_plan 
		inner Join `tabWork Order Operation` woo
		on woo.parent = wo.name 
		LEFT join `tabProduction Plan Material Request` ppmr
		on pp.name = ppmr.parent and pp.get_items_from = 'Material Request'
		LEFT join `tabMaterial Request Item` mri 
		on ppmr.material_request = mri.parent
		where pp.docstatus = 1 
		) as t1 where t1.blanket_order is not null {conditions}""".format(conditions=conditions)
	inhouse_orders=frappe.db.sql(query, as_dict=True)
	return inhouse_orders


def get_subcontract_data(filters,conditions):
	#returns purchase_order, blanket_order details form production plan
	query="""SELECT t1.production_plan, t1.blanket_order, t1.work_order, t1.doctype, t1.style, t1.process, t1.workstation, 
	COALESCE(t1.issue_qty,0) as "issue_qty", COALESCE(t1.receive_qty,0) as "receive_qty", COALESCE((t1.issue_qty-t1.receive_qty),0) as "balance_qty", 
	COALESCE(t1.reject_qty, 0) as "reject_qty", COALESCE(t1.returned_qty,0) as "returned_qty" from
		(SELECT DISTINCT
		tpp.name as "production_plan",
		(CASE WHEN tpp.get_items_from = 'Sales Order' THEN tsoi.blanket_order ELSE tmri.blanket_order END) as "blanket_order",
		poi.parent as "work_order",
		"Purchase Order" as doctype,
		(CASE WHEN tpp.get_items_from = 'Sales Order' THEN (SELECT ti.variant_of from `tabItem` ti where ti.name = tsoi.item_code)
		ELSE (SELECT mti.variant_of from `tabItem` mti where mti.name = tmri.item_code)END) as "style",
		(SELECT bo.operation from `tabBOM Operation` bo WHERE bo.parent = poi.bom) as "process",
		(SELECT po.supplier from `tabPurchase Order` po where po.name = poi.parent) as "workstation",
		(SELECT sum(pois.supplied_qty) from `tabPurchase Order Item Supplied`
		 pois inner join `tabItem` it on it.item_code = pois.rm_item_code
		 where pois.parent = poi.parent and poi.item_code = pois.main_item_code and (it.fabric_or_yarn = 1 or it.intermediate_product = 1))  as "issue_qty",
		poi.received_qty as "receive_qty",
		(Select sum(pri.rejected_qty) from `tabPurchase Receipt Item` pri where poi.parent = pri.purchase_order and poi.item_code = pri.item_code) as "reject_qty",
		(SELECT sum(pois.returned_qty) from `tabPurchase Order Item Supplied` pois
		 inner join `tabItem` it on it.item_code = pois.rm_item_code 
		 where pois.parent = poi.parent and poi.item_code = pois.main_item_code and (it.fabric_or_yarn = 1 or it.intermediate_product = 1)) as "returned_qty"
		from `tabProduction Plan` tpp 
		LEFT join `tabProduction Plan Sales Order` tppso
		on tpp.name = tppso.parent
		LEFT join `tabSales Order Item` tsoi
		on tppso.sales_order = tsoi.parent and tpp.get_items_from = 'Sales Order'
		inner join `tabPurchase Order Item` poi
		on poi.production_plan = tpp.name
		LEFT join `tabProduction Plan Material Request` tppmr
		on tpp.name = tppmr.parent and tpp.get_items_from = 'Material Request'
		LEFT join `tabMaterial Request Item` tmri
		on tppmr.material_request = tmri.parent 
		where tpp.docstatus =1
		) as t1 where t1.blanket_order is not null {conditions}""".format(conditions=conditions)
	subcontract_orders=frappe.db.sql(query, as_dict=True)
	return subcontract_orders
	
	
def get_conditions(filters):
	conditions=""
	if filters.get('blanket_order'):
		conditions += " AND t1.blanket_order = '{}'".format(filters.get('blanket_order'))
	if filters.get('item'):
		conditions += " AND  t1.style = '{}'".format(filters.get('item'))
	if filters.get('work_order') and not filters.get('purchase_order'):
		conditions += " AND  t1.work_order = '{}'".format(filters.get('work_order'))
	if not filters.get('work_order') and  filters.get('purchase_order'):
		conditions += " AND  t1.work_order = '{}'".format(filters.get('purchase_order'))
	if filters.get('work_order') and filters.get('purchase_order'):
		conditions += " AND  t1.work_order = '{}'".format(filters.get('work_order'))
		conditions += " OR  t1.work_order = '{}'".format(filters.get('purchase_order'))
	if filters.get('production_plan'):
		conditions += " AND  t1.production_plan = '{}'".format(filters.get('production_plan'))
	return conditions