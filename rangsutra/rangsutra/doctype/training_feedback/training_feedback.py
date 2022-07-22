# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt


import frappe
from frappe import _
from frappe.model.document import Document
from erpnext.hr.doctype.training_feedback.training_feedback import TrainingFeedback


class CustomTrainingFeedback(TrainingFeedback):
	def validate(self):
		training_event = frappe.get_doc("Training Event", self.training_event)
		if training_event.docstatus != 1:
			frappe.throw(_("{0} must be submitted").format(_("Training Event")))

		if self.is_artisan_training == 0:
			emp_event_details = frappe.db.get_value("Training Event Employee", {
				"parent": self.training_event,
				"employee": self.employee
			}, ["name", "attendance"], as_dict=True)

			if not emp_event_details:
				frappe.throw(_("Employee {0} not found in Training Event Participants.").format(
					frappe.bold(self.employee_name)))

			if emp_event_details.attendance == "Absent":
				frappe.throw(_("Feedback cannot be recorded for an absent Employee."))
		else:
			artisan_event_details = frappe.db.get_value("Training Event Artisan", {
				"parent": self.training_event,
				"artisan": self.artisan
			}, ["name", "attendance"], as_dict=True)

			if not artisan_event_details:
				frappe.throw(_("Artisan {0} not found in Training Event Participants.").format(
					frappe.bold(self.artisan_name)))

			if artisan_event_details.attendance == "Absent":
				frappe.throw(_("Feedback cannot be recorded for an absent Artisan."))

	def on_submit(self):
		if self.is_artisan_training == 0:
			employee = frappe.db.get_value("Training Event Employee", {
				"parent": self.training_event,
				"employee": self.employee
			})

			if employee:
				frappe.db.set_value("Training Event Employee", employee, "status", "Feedback Submitted")
		else:
			artisan = frappe.db.get_value("Training Event Artisan", {
				"parent": self.training_event,
				"artisan": self.artisan
			})

			if artisan:
				frappe.db.set_value("Training Event Artisan", artisan, "status", "Feedback Submitted")

	def on_cancel(self):
		if self.is_artisan_training == 0:
			employee = frappe.db.get_value("Training Event Employee", {
				"parent": self.training_event,
				"employee": self.employee
			})

			if employee:
				frappe.db.set_value("Training Event Employee", employee, "status", "Completed")
		else:
			artisan = frappe.db.get_value("Training Event Artisan", {
				"parent": self.training_event,
				"artisan": self.artisan
			})

			if artisan:
				frappe.db.set_value("Training Event Artisan", artisan, "status", "Completed")