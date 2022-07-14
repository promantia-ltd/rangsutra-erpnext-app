# Copyright (c) 2022, rangsutra_app and contributors
# For license information, please see license.txt

from itertools import count
from multiprocessing.sharedctypes import Value
import frappe
from frappe import _
from frappe.model.document import Document
import json

class VariantBOMGenerator(Document):
	def validate(self):
		for row in self.raw_materials:
			if row.qty == 0 or row.qty == None:
				frappe.throw(_("Raw Materials quantity cannot be 0."))

			if row.operation == None:
				frappe.throw(_("Operations cannot be null."))

	@frappe.whitelist()
	def get_variant_items(self):
		items = []
		for item in frappe.db.get_list("Item",{"variant_of":self.finished_good_item},["item_code","item_name"]):
			items.append(dict(
				item_code = item.item_code,
				item_name = item.item_name
			))

		return items

	@frappe.whitelist()
	def get_operations(self):
		operations = []
		for operation in frappe.db.get_list("BOM Operation",{"parent":self.routing,"parenttype":"Routing"},"operation"):
			operations.append(dict(
				operation = operation.operation
			))
		return operations

	@frappe.whitelist()
	def get_item_filter(self):
		return frappe.db.sql("""select item_code from `tabItem` where variant_of IS NULL AND is_finished_product != 1 AND intermediate_product != 1 """,as_dict = True)


@frappe.whitelist()
def generate_variant_template_bom(doc,items):
	error_log = ''
	doc = json.loads(doc)
	items = json.loads(items).get('items')
	for row_item in items:
		color_attribute = None
		color = None
		size_attribute = None
		size = None
		previous_bom_item = None
		previous_bom_item_name = None
		attributes = frappe.db.get_list("Item Variant Attribute",{"parent":row_item['item_code'],"parenttype":"Item"},["attribute","attribute_value"])
		attributes_copy = attributes
		for i in range(len(attributes)):
			for j in range(len(attributes_copy)):
				if ("color" in attributes_copy[j].get('attribute').lower() or "colour" in attributes_copy[j].get('attribute').lower()):
					color_attribute = attributes_copy[j].get('attribute')
					color = attributes_copy[j].get('attribute_value')
					del attributes_copy[j]
					break
				if ("size" in attributes_copy[j].get('attribute').lower()):
					size_attribute = attributes_copy[j].get('attribute')
					size = attributes_copy[j].get('attribute_value')
					del attributes_copy[j]
					break

		attributes = attributes_copy

		for ope in frappe.db.get_list("BOM Operation",{"parent":doc['routing'],"parenttype":"Routing"},["operation","sequence_id"], order_by="sequence_id asc"):
			intermediate_item,intermediate_item_name = get_intermediate_item(doc, color_attribute,color,size_attribute,size,ope.operation)

			if intermediate_item:
				count = 0
				if ope.sequence_id == 1:
					for row in doc['raw_materials']:
						if row['operation'] == ope.operation:
							count = count + 1
					if count < 1:
						error_log = error_log+"There is no raw materials for the operation {0}<br>".format(ope.operation)

				create_bom(doc,color_attribute,color,size_attribute,size, intermediate_item, intermediate_item_name, ope.sequence_id, ope.operation, previous_bom_item, previous_bom_item_name, with_operation = 1)
				previous_bom_item = intermediate_item
				previous_bom_item_name = intermediate_item_name
			else:
				error_log = error_log+'There is no Intermediate item for the operation '+str(ope.operation)+'<br>'
				break

		if intermediate_item:	
			create_bom(doc,color_attribute,color,size_attribute,size, row_item['item_code'], row_item['item_name'], sequence_id = 2, operation = None, previous_bom_item = previous_bom_item, previous_bom_item_name = previous_bom_item_name, with_operation = 0)
	frappe.db.set_value('Variant BOM Generator', doc['name'], 'error_details', error_log)

	if error_log:
		return "Failed"
	else:
		return "success"
	

def get_intermediate_item(doc, color_attribute,color,size_attribute,size,operation):
	intermediate_item = None
	intermediate_item_name = None
	for color_item in frappe.db.sql("""select i.item_code from `tabItem` i
	join `tabItem Variant Attribute` iva on iva.parent = i.item_code 
	where i.variant_of = '{variant_item}' and iva.attribute = '{color_attribute}' and iva.attribute_value = '{color}'
	""".format(variant_item = doc['associated_intermediate_item'],
	color_attribute = color_attribute,
	color = color
	),as_dict=True):
		for stage_item in frappe.db.sql("""select i.item_code, i.item_name from `tabItem` i
		join `tabItem Variant Attribute` iva on iva.parent = i.item_code 
		where i.item_code = '{item_code}' and iva.attribute = 'Stage' and iva.attribute_value = '{stage}'
		""".format(item_code = color_item.item_code,
		stage = operation
		),as_dict=True):
			for size_item in frappe.db.sql("""select i.item_code, i.item_name from `tabItem` i
			join `tabItem Variant Attribute` iva on iva.parent = i.item_code 
			where i.item_code = '{item_code}' and iva.attribute LIKE '%{size_attribute}%' and iva.attribute_value = '{size}' limit 1
			""".format(item_code = stage_item.item_code,
			size_attribute = size_attribute,
			size = size
			),as_dict=True):
				intermediate_item = size_item.item_code
				intermediate_item_name = size_item.item_name

			if intermediate_item:
				break
	
	return intermediate_item, intermediate_item_name


def create_bom(doc,color_attribute,color,size_attribute,size, bom_item, bom_item_name, sequence_id, operation = None, previous_bom_item = None, previous_bom_item_name = None, with_operation = None):
	count = 0
	old_bom_name = frappe.db.get_value("BOM",{"item":bom_item, "docstatus":1,"is_default":1,"is_active":1},"name")
	if old_bom_name:
		old_bom_item = frappe.db.get_list("BOM Item",{"parenttype":"BOM","parent":old_bom_name},"item_code")
		old_bom_items = [value for elem in old_bom_item for value in elem.values()]
		for val in doc['raw_materials']:
			if val['operation'] == operation:
				if val['has_variants'] != 1:
					if val['item_code'] not in old_bom_items:
						count = count+1
				else:
					i_code,i_name=get_raw_materials(val['item_code'],color_attribute,color,size_attribute,size)
					if i_code not in old_bom_items:
						count = count+1
	else:	 
		count = count+1

	if count > 0:
		bom_doc=frappe.get_doc(dict(doctype = 'BOM',
			item = bom_item,
			item_name = bom_item_name,
			is_active = 1,
			is_default = 1,
			quantity = 1,
			with_operations = with_operation,
			transfer_material_against = 'Work Order',
			routing = operation
		))
		if sequence_id > 1:
			bom_doc.append('items', {
				"item_code":previous_bom_item,
				"item_name":previous_bom_item_name,
				"qty":1
			})
		for val in doc['raw_materials']:
			if val['operation'] == operation:
				if val['has_variants'] != 1:
					item_code = val['item_code']
					item_name = val['item_name']
				else:
					item_code,item_name=get_raw_materials(val['item_code'],color_attribute,color,size_attribute,size)
					if not item_code:
						continue
				bom_doc.append('items', {
					"item_code":item_code,
					"item_name":item_name,
					"qty":val['qty'],
					"uom":val['uom']
				})
		bom_doc.submit()


def get_raw_materials(template_item_code,color_attribute,color,size_attribute,size):
	raw_item_code = None
	raw_item_name = None
	for color_item in frappe.db.sql("""select i.item_code, i.item_name from `tabItem` i
	join `tabItem Variant Attribute` iva on iva.parent = i.item_code 
	where i.variant_of = '{variant_item}' and iva.attribute = '{color_attribute}' and iva.attribute_value = '{color}'
	""".format(variant_item = template_item_code,
	color_attribute = color_attribute,
	color = color
	),as_dict=True):
		raw_item_code = color_item.item_code
		raw_item_name = color_item.item_name
		for size_item in frappe.db.sql("""select i.item_code, i.item_name from `tabItem` i
		join `tabItem Variant Attribute` iva on iva.parent = i.item_code 
		where i.item_code = '{item_code}' and iva.attribute LIKE '%{size_attribute}%' and iva.attribute_value = '{size}' limit 1
		""".format(item_code = color_item.item_code,
		size_attribute = size_attribute,
		size = size
		),as_dict=True):
			raw_item_code = size_item.item_code
			raw_item_name = size_item.item_name
	return raw_item_code,raw_item_name
