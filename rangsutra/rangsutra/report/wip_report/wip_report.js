// Copyright (c) 2016, rangsutra_app and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["WIP Report"] = {
	"filters": [
		{
			"fieldname":"company",
			"label": __("Company"),
			"fieldtype": "Link",
			"options": "Company",
			"reqd": 1,
			"default": frappe.defaults.get_user_default("Company")
		},
		{
			"fieldname":"blanket_order",
			"label": __("Blanket Order"),
			"fieldtype": "Link",
			"options": "Blanket Order",
			"reqd": 0
		},
		{
			"fieldname":"item",
			"label": __("Item"),
			"fieldtype": "Link",
			"options": "Item",
			"reqd": 0,
			get_query: () => {
				var company = frappe.query_report.get_filter_value('item');
				return {
					filters: {
						'has_variants': 1
					}
				}
			}
		},
		{
			"fieldname":"work_order",
			"label": __("Work Order"),
			"fieldtype": "Link",
			"options": "Work Order",
			"reqd": 0
		},
		{
			"fieldname":"purchase_order",
			"label": __("Purchase Order"),
			"fieldtype": "Link",
			"options": "Purchase Order",
			"reqd": 0
		},
		{
			"fieldname":"production_plan",
			"label": __("Production Plan"),
			"fieldtype": "Link",
			"options": "Production Plan",
			"reqd": 0
		}
	]
};
