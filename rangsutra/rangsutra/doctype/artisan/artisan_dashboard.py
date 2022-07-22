
from frappe import _


def get_data():
	return {
		'fieldname': 'artisan',
		'transactions': [
			{
				'label': _('Training'),
				'items': ['Training Event', 'Training Result', 'Training Feedback']
			}
		]
	}
