# Copyright (c) 2022, rangsutra_app and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt

class CraftOrder(Document):
	def validate(self):
		print(self.items)
		if not self.items:
			frappe.throw(_("Items table cannot be empty."))

		for row in self.items:
			receive_qty = 0
			balance_qty = 0
			if row.receive_qty:
				receive_qty = row.receive_qty

			if receive_qty > row.total_qty:
				frappe.throw(_("Receive Qty cannot be greater then Total Qty"))


			if row.balance_qty:
				balance_qty = row.balance_qty
			if row.total_qty < (receive_qty+balance_qty):
				frappe.throw(_("Balance Qty cannot be greater then Total Qty"))

	def on_submit(self):
		update_issued_qty(self)

	def on_cancel(self):
		update_issued_qty(self)


def update_issued_qty(self):
	for row in self.raw_materials_issued:
		total_issued_qty = frappe.db.sql("""select sum(crmi.issued_qty) as total_issued_qty from `tabCraft Order Raw Materials Issued` crmi join `tabCraft Order` co on co.name = crmi.parent  where co.purchase_order = '{purchase_order}' and co.docstatus=1 and crmi.subcontracted_item_code = '{subcontracted_item_code}' and crmi.raw_materials_issue_item_code = '{raw_materials_issue_item_code}' """.format(purchase_order = self.purchase_order,
		subcontracted_item_code = row.subcontracted_item_code,
		raw_materials_issue_item_code = row.raw_materials_issue_item_code
	), as_dict=1)
		total_issued_qty = total_issued_qty[0]['total_issued_qty'] or 0
		sub_contract_item_name = frappe.db.get_value("Purchase Order Item Supplied",{"main_item_code":row.subcontracted_item_code,"rm_item_code":row.raw_materials_issue_item_code,"parent":self.purchase_order},'name')
		frappe.db.set_value('Purchase Order Item Supplied', sub_contract_item_name, 'issued_qty', total_issued_qty)


@frappe.whitelist()
def get_remaining_issue_qty(subcontracted_item_code,raw_materials_issue_item_code,purchase_order):
	total_issued_qty = frappe.db.sql("""select sum(crmi.issued_qty) as total_issued_qty from `tabCraft Order Raw Materials Issued` crmi join `tabCraft Order` co on co.name = crmi.parent  where co.purchase_order = '{purchase_order}' and co.docstatus=1 and crmi.subcontracted_item_code = '{subcontracted_item_code}' and crmi.raw_materials_issue_item_code = '{raw_materials_issue_item_code}' """.format(purchase_order = purchase_order,
		subcontracted_item_code = subcontracted_item_code,
		raw_materials_issue_item_code = raw_materials_issue_item_code
	), as_dict=1)
	total_issued_qty = total_issued_qty[0]['total_issued_qty'] or 0

	return total_issued_qty