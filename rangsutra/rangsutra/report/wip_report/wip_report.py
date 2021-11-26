# Copyright (c) 2013, rangsutra_app and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _

def execute(filters=None):
	columns = get_columns()
	conditions = get_conditions(filters)
	data = get_data(filters,conditions)
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

def get_data(filters,conditions):
	query="""SELECT t1.production_plan, t1.blanket_order, t1.work_order, t1.doctype, t1.style, t1.process, t1.workstation, COALESCE(t1.issue_qty,0) as "issue_qty", COALESCE(t1.receive_qty,0) as "receive_qty", COALESCE((t1.issue_qty-t1.receive_qty),0) as "balance_qty", COALESCE(t1.reject_qty, 0) as "reject_qty", COALESCE(t1.returned_qty,0) as "returned_qty" from
		(SELECT DISTINCT
		pp.name as "production_plan",
		soi.blanket_order,
		wo.name as "work_order",
		"Work Order" as doctype,
		(SELECT i.variant_of from `tabItem` i where i.name = soi.item_code) as "style",
		woo.operation as "process",
		woo.workstation ,
		(SELECT SUM(woi.transferred_qty) from `tabWork Order Item` woi inner join `tabItem` fti on woi.item_code = fti.name
		where woi.parent = wo.name and (fti.fabric_or_yarn = 1 or fti.intermediate_product = 1) GROUP BY woi.parent) as "issue_qty",
		wo.produced_qty as "receive_qty",
		(SELECT sum(se.fg_completed_qty) from `tabStock Entry` se where se.work_order = wo.name and se.stock_entry_type = 'Manufacturing Reject') as "reject_qty",
		(SELECT sum(se.fg_completed_qty) from `tabStock Entry` se where se.work_order = wo.name and se.stock_entry_type = 'Manufacturing Return') as "returned_qty"
		from `tabProduction Plan` pp 
		inner join `tabProduction Plan Sales Order` ppso
		on pp.name = ppso.parent
		inner join `tabSales Order Item` soi
		on ppso.sales_order = soi.parent 
		inner join `tabWork Order` wo
		on pp.name = wo.production_plan 
		inner Join `tabWork Order Operation` woo
		on woo.parent = wo.name 
		where pp.docstatus = 1
		UNION 
		SELECT DISTINCT
		tpp.name as "production_plan",
		tsoi.blanket_order,
		poi.parent as "work_order",
		"Purchase Order" as doctype,
		(SELECT ti.variant_of from `tabItem` ti where ti.name = tsoi.item_code) as "style",
		(SELECT bo.operation from `tabBOM Operation` bo WHERE bo.parent = poi.bom) as "process",
		(SELECT po.supplier from `tabPurchase Order` po where po.name = poi.parent) as "workstation",
		(SELECT sum(pois.supplied_qty) from `tabPurchase Order Item Supplied`
		 pois inner join `tabItem` it on it.item_code = pois.main_item_code
		 where pois.parent = poi.parent and poi.item_code = pois.main_item_code and (it.fabric_or_yarn = 1 or it.intermediate_product = 1))  as "issue_qty",
		poi.received_qty as "receive_qty",
		pri.rejected_qty as "reject_qty",
		(SELECT sum(pois.returned_qty) from `tabPurchase Order Item Supplied` pois
		 inner join `tabItem` it on it.item_code = pois.main_item_code 
		 where pois.parent = poi.parent and poi.item_code = pois.main_item_code and (it.fabric_or_yarn = 1 or it.intermediate_product = 1)) as "returned_qty"
		from `tabProduction Plan` tpp 
		inner join `tabProduction Plan Sales Order` tppso
		on tpp.name = tppso.parent
		inner join `tabSales Order Item` tsoi
		on tppso.sales_order = tsoi.parent
		inner join `tabPurchase Order Item` poi
		on poi.production_plan = tpp.name
		left join `tabPurchase Receipt Item` pri
		on poi.parent = pri.purchase_order and poi.item_code = pri.item_code 
		where tpp.docstatus =1
		UNION 
		SELECT 
		mpp.name as "production_plan",
		mri.blanket_order ,
		mwo.name as "work_order",
		"Work Order" as doctype,
		(SELECT mi.variant_of from `tabItem` mi where mi.name = mri.item_code) as "style",
		mwoo.operation as "process",
		mwoo.workstation ,
		(SELECT SUM(mwoi.transferred_qty) from `tabWork Order Item` mwoi inner join `tabItem` mti on mwoi.item_code = mti.name
		where mwoi.parent = mwo.name and (mti.fabric_or_yarn = 1 or mti.intermediate_product = 1) GROUP BY mwoi.parent) as "issue_qty",
		mwo.produced_qty as "receive_qty",
		(SELECT sum(mse.fg_completed_qty) from `tabStock Entry` mse where mse.work_order = mwo.name and mse.stock_entry_type = 'Manufacturing Reject') as "reject_qty",
		(SELECT sum(mse.fg_completed_qty) from `tabStock Entry` mse where mse.work_order = mwo.name and mse.stock_entry_type = 'Manufacturing Return') as "returned_qty"
		FROM `tabProduction Plan` mpp 
		inner join `tabProduction Plan Material Request` ppmr
		on mpp.name = ppmr.parent 
		inner join `tabMaterial Request Item` mri 
		on ppmr.material_request = mri.parent 
		inner join `tabWork Order` mwo 
		on mpp.name = mwo.production_plan 
		inner Join `tabWork Order Operation` mwoo
		on mwoo.parent = mwo.name 
		where mpp.docstatus = 1
		UNION 
		SELECT 
		mtpp.name as "production_plan",
		tmri.blanket_order,
		mpoi.parent as "work_order",
		"Purchase Order" as doctype,
		(SELECT mti.variant_of from `tabItem` mti where mti.name = tmri.item_code) as "style",
		(SELECT mbo.operation from `tabBOM Operation` mbo WHERE mbo.parent = mpoi.bom) as "process",
		(SELECT mpo.supplier from `tabPurchase Order` mpo where mpo.name = mpoi.parent) as "workstation",
		(SELECT sum(tpois.supplied_qty) from `tabPurchase Order Item Supplied` tpois
		 inner join `tabItem` it on it.item_code = tpois.main_item_code 
		 where tpois.parent = mpoi.parent and mpoi.item_code = tpois.main_item_code and (it.fabric_or_yarn = 1 or it.intermediate_product = 1)) as "issue_qty",
		mpoi.received_qty as "receive_qty",
		mpri.rejected_qty as "reject_qty",
		(SELECT sum(tpois.returned_qty) from `tabPurchase Order Item Supplied` tpois
		 inner join `tabItem` it on it.item_code = tpois.main_item_code 
		 where tpois.parent = mpoi.parent and mpoi.item_code = tpois.main_item_code and (it.fabric_or_yarn = 1 or it.intermediate_product = 1)) as "returned_qty"
		from `tabProduction Plan` mtpp 
		inner join `tabProduction Plan Material Request` tppmr
		on mtpp.name = tppmr.parent 
		inner join `tabMaterial Request Item` tmri
		on tppmr.material_request = tmri.parent 
		inner join `tabPurchase Order Item` mpoi
		on mpoi.production_plan = mtpp.name 
		left join `tabPurchase Receipt Item` mpri
		on mpoi.parent = mpri.purchase_order and mpoi.item_code = mpri.item_code
		WHERE mtpp.docstatus =1
		) as t1 where t1.blanket_order is not null {conditions}""".format(conditions=conditions)
	orders=frappe.db.sql(query, as_dict=True)
	return orders
	
	
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