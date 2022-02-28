from __future__ import unicode_literals
from frappe import _


def get_dashboard_data(data):
	return {
		'heatmap': True,
		'heatmap_message': _('This is based on the Time Sheets created against this project'),
		'fieldname': 'project',
		'transactions': [
			{
				'label': _('Project'),
				'items': ['Task', 'Timesheet', 'Expense Claim', 'Issue' , 'Project Update']
			},
			{
				'label': _('Material'),
				'items': ['Material Request', 'BOM', 'Stock Entry','Production Plan']
			},
			{
				'label': _('Sales'),
				'items': ['Sales Order', 'Delivery Note', 'Sales Invoice']
			},
			{
				'label': _('Purchase'),
				'items': ['Purchase Order', 'Purchase Receipt', 'Purchase Invoice']
			},
		]
	}
