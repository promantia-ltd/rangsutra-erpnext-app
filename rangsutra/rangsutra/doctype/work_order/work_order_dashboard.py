from __future__ import unicode_literals

from frappe import _


def get_dashboard_data(data):
	return {
		'fieldname': 'work_order',
		'non_standard_fieldnames': {
			'Batch': 'reference_name'
		},
		'internal_links': {
			'Production Plan': 'production_plan'
		},
		'transactions': [
			{
				'label': _('Transactions'),
				'items': ['Stock Entry', 'Job Card', 'Pick List']
			},
			{
				'label': _('Reference'),
				'items': ['Serial No', 'Batch', 'Production Plan']
			}
		]
	}
