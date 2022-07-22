import frappe
from frappe import _
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc

@frappe.whitelist()
def make_craft_order(source_name, target_doc=None):
    def update_item(obj, target, source_parent):
        target.conversion_factor = 1.0

    doclist = get_mapped_doc("Purchase Order", source_name, {
		"Purchase Order": {
			"doctype": "Craft Order",
		},
		"Purchase Order Item": {
			"doctype": "Craft Order Items",
			"field_map": {
				"item_code": "subcontracted_item_code",
                "item_name" : "subcontracted_item_name",
				"uom": "uom"
            },
			"postprocess": update_item
		}
	}, target_doc)

    return doclist
