# Copyright (c) 2022, rangsutra_app and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import json

class VariantBOMGenerator(Document):
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
def get_item_filter(doctype, txt, searchfield, start, page_len, filters):
	return frappe.db.sql("""select item_code from `tabItem` where has_variants = 1 or variant_of IS NULL """)


@frappe.whitelist()
def generate_variant_template_bom(doc,items):
	items = json.loads(items).get('items')
	for i in items:
		color_attribute = None
		color = None
		country_attribute = None
		country = None
		attributes = frappe.db.get_list("Item Variant Attribute",{"parent":i['item_code'],"parenttype":"Item"},["attribute","attribute_value"])
		attributes_copy = attributes
		for i in range(len(attributes)):
			for j in range(len(attributes_copy)):
				if ("color" in attributes_copy[j].get('attribute').lower() or "colour" in attributes_copy[j].get('attribute').lower()):
					color_attribute = attributes_copy[j].get('attribute')
					color = attributes_copy[j].get('attribute_value')
					del attributes_copy[j]
					break
				if "country code" in attributes_copy[j].get('attribute').lower():
					country_attribute = attributes_copy[j].get('attribute')
					country = attributes_copy[j].get('attribute_value')
					del attributes_copy[j]
					break
		attributes = attributes_copy
		print(attributes)
	return attributes
