# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt
import frappe
from frappe import _

@frappe.whitelist()
def get_artisans(training_event):
	return frappe.get_doc("Training Event", training_event).artisans
