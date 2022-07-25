# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "rangsutra"
app_title = "Rangsutra"
app_publisher = "rangsutra_app"
app_description = "rangsutra_app"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "rangsutra_app@gmail.com"
app_license = "MIT"



fixtures = ["Server Script","Item Variant Settings","Workflow","Workflow State","Workflow Action Master",
{
    "dt":"DocType",
    "filters":[
        [
        "name","in",[
		"Style Details",
		"Collection Details",
		"Launch Details",
		"Craft",
		"Length",
		"Sleeve Length",
		"Cluster",
		"Wash",
		"Fit",
		"Neck",
		"Fabric",
		"Material",
		"Material Type",
		"Warp Count",
		"Material Process",
		"Weft Count"
        ]
    ]
]
},
{"dt": "Custom Field",
		"filters": [
         [
             "name", "in", [
		"Brand-brand_code",
		"Item-brand_code",
		"Item-launch_year",
		"Item-collection_code",
		"Item-style_number",
		"Item Group-category_code",
		"Item Group-sub_category_code",
		"POS Invoice-transaction_id",
		"Sales Invoice Payment-transaction_id",
		"Item-updated_item",
		"Item-item_details",
		"Item-column_break_30",
		"Delivery Note-tracking_id",
		"Item Barcode-system_generated_barcode",
		"Warehouse-warehouse_manager",
		"Item-length",
		"Item-sleeve_length",
		"Item-cluster",
		"Item-wash",
		"Item-craft",
		"Item-fit",
		"Item-neck",
		"Item-fabric",
		"Sales Invoice Payment-payment_source",
		"POS Invoice-payment_source",
		"Sales Invoice-delivery_note",
		"Sales Invoice-destination",
		"Sales Invoice-financial_year",
		"Sales Invoice-dispatch_document_no",
		"Item-print_label_quantity",
		"Packing Slip-box_no",
		"Item-print_name",
		"Sales Order-financial_year",
		"POS Invoice-financial_year",
		"Stock Entry-financial_year",
		"Stock Reconciliation-financial_year",
		"Material Request-financial_year",
		"Delivery Note-financial_year",
		"Packing Slip-financial_year",
		"Pick List-financial_year",
		"Purchase Order-financial_year",
		"Purchase Invoice-financial_year",
		"Purchase Receipt-financial_year",
		"Payment Order-financial_year",
		"Payment Entry-financial_year",
		"Payment Request-financial_year",
		"Delivery Note-dispatch_document_no",
		"Delivery Note-destination",
		"Sales Invoice-export_details",
		"Sales Invoice-iec",
		"Sales Invoice-lut",
		"Sales Invoice-supplier_no",
		"Sales Invoice-place_of_receipt",
		"Sales Invoice-vessel_voyage_no",
		"Sales Invoice-port_of_loading",
		"Sales Invoice-port_of_discharge",
		"Sales Invoice-column_break_184",
		"Sales Invoice-fca",
		"Sales Invoice-destination_code",
		"Sales Invoice-gross_weight",
		"Sales Invoice-total_cbm",
		"Sales Invoice-district_code",
		"Sales Invoice-pta_fta_code",
		"Sales Invoice-consignment_no",
		"Item-intermediate_product",
		"Item-raw_materials_details",
		"Item-material",
		"Item-composition",
		"Item-type",
		"Item-column_break_48",
		"Item-count",
		"Item-process",
		"Item-fabric_or_yarn",
		"Payment Entry-utr_number",
		"Item-is_finished_product",
		"Purchase Receipt-purchase_order",
		"Purchase Order-branch_abbr",
		"Purchase Invoice-branch_abbr",
		"Purchase Receipt-branch_abbr",
		"Sales Order-branch_abbr",
		"Sales Invoice-branch_abbr",
		"Delivery Note-branch_abbr",
		"Stock Reconciliation-branch_abbr",
		"POS Invoice-branch_abbr",
		"Material Request-branch_abbr",
		"Packing Slip-branch_abbr",
		"Pick List-branch_abbr",
		"Stock Entry-branch_abbr",
		"Payment Entry-branch_abbr",
		"Payment Request-branch_abbr",
		"Payment Order-branch_abbr",
		"Quality Inspection-accepted_qty",
		"Quality Inspection-rejected_qty",
		"Item-no_of_yarns",
		"Packing Slip Item-box_no",
		"Packing Slip Item-box_measurement",
		"Packing Slip Item-gross_weight",
		"Sales Invoice Item-package_no",
		"Sales Invoice Item-dbk_no",
		"Packing Slip-sales_invoice",
		"Purchase Receipt-supplier_delivery_date",
		"Item-weft_count",
		"Stock Entry-transporter_info",
		"Stock Entry-transporter",
		"Stock Entry-gst_transporter_id",
		"Stock Entry-driver",
		"Stock Entry-transport_receipt_no",
		"Stock Entry-vehicle_no",
		"Stock Entry-distance",
		"Stock Entry-column_break_79",
		"Stock Entry-transporter_name",
		"Stock Entry-mode_of_transport",
		"Stock Entry-destination",
		"Stock Entry-driver_name",
		"Stock Entry-transport_receipt_date",
		"Stock Entry-gst_vehicle_type",
		"Stock Entry-section_break_46",
		"Stock Entry-taxes",
		"Item-is_sample_product",
		"Stock Entry-total",
		"Stock Entry-net_total",
		"Item-is_other_raw_material",
		"Material Request-blanket_order",
		"Material Request Item-blanket_order",
		"Quality Inspection-supplier",
		"Item-dbk_no",
		"Sales Invoice-sqc",
		"Blanket Order-financial_year",
		"Quality Inspection-financial_year",
		"Quality Inspection-branch_abbr",
		"Production Plan-financial_year",
		"Landed Cost Voucher-financial_year",
		"Landed Cost Voucher-branch_abbr",
		"Job Card-branch_abbr",
		"Asset-financial_year",
		"Asset-branch_abbr",
		"Journal Entry-financial_year",
		"Journal Entry-branch_abbr",
		"Purchase Order-project",
		"Material Request-project",
		"Sales Invoice-notif_party_one_address",
		"Sales Invoice-notif_party_one_contact",
		"Sales Invoice-notif_party_two_address",
		"Sales Invoice-notif_party_two_contact",
		"Sales Invoice-bank_account",
		"Sales Invoice-gst_state_name",
		"Purchase Invoice-gst_state_name",
		"Employee-section_break_110",
		"Employee-comments",
		"Employee-line_manager",
		"Employee-aadhar_card",
		"Production Plan-production_plan_name",
		"Purchase Taxes and Charges Template-is_rcm",
		"Stock Entry-suppliers_name",
		"Stock Entry-suppliers_address",
		"Stock Entry-suppliers_address_details",
		"Stock Entry Detail-total_qty",
		"Purchase Order Item Supplied-total_qty",
		"Purchase Order Item Supplied-issued_qty",
		"Training Event-is_artisan_training",	
		"Training Event-artisans",	
		"Training Feedback-is_artisan_training",	
		"Training Feedback-artisan",	
		"Training Feedback-artisan_name",	
		"Training Result-is_artisan_training",	
		"Training Result-artisans",
		"Location-address",
		"Location-address_display",
		"Supplier-location_list",
		"Supplier-location_details"
		]
	]
]
},
{"dt": "Property Setter",
		"filters": [
         [
             "name", "in", [
		"Purchase Order-shipping_address-label",
		"Item-brand-mandatory_depends_on",
		"Item-brand-read_only_depends_on",
		"Sales Invoice-naming_series-options",
		"Packing Slip-to_case_no-hidden",
		"Packing Slip-from_case_no-hidden",
		"Sales Order-naming_series-options",
		"POS Invoice-naming_series-options",
		"Stock Reconciliation-naming_series-options",
		"Stock Entry-naming_series-options",
		"Material Request-naming_series-options",
		"Delivery Note-naming_series-options",
		"Packing Slip-naming_series-options",
		"Pick List-naming_series-options",
		"Purchase Order-naming_series-options",
		"Purchase Invoice-naming_series-options",
		"Purchase Receipt-naming_series-options",
		"Payment Order-naming_series-default",
		"Payment Order-naming_series-options",
		"Payment Entry-naming_series-options",
		"Payment Request-naming_series-options",
		"Sales Invoice-naming_series-default",
		"Payment Entry-naming_series-default",
		"Sales Invoice-main-default_print_format",
		"Purchase Receipt-main-default_print_format",
		"Purchase Order-main-default_print_format",
		"Delivery Note-main-default_print_format",
		"Packing Slip Item-item_name-options",
		"Blanket Order-naming_series-options",
		"Quality Inspection-naming_series-options",
		"Production Plan-naming_series-options",
		"Landed Cost Voucher-naming_series-options",
		"Job Card-naming_series-options",
		"Job Card-naming_series-default",
		"Asset-naming_series-options",
		"Journal Entry-naming_series-options",
		"Item Default-expense_account-in_list_view",
		"Item Default-income_account-in_list_view",
		"Sales Order Item-item_tax_template-in_list_view",
		"Sales Order Item-item_code-columns",
		"Sales Order Item-item_tax_template-columns",
		"Sales Order Item-delivery_date-columns",
		"Production Plan Sub Assembly Item-supplier-in_list_view",
		"Production Plan Sub Assembly Item-schedule_date-in_list_view",
		"Stock Entry Detail-batch_no-in_list_view",
		"Stock Entry Detail-actual_qty-in_list_view",
		"Stock Entry Detail-s_warehouse-columns",
		"Stock Entry Detail-t_warehouse-columns",
		"Stock Entry Detail-qty-columns",
		"Stock Entry Detail-batch_no-columns",
		"Stock Entry Detail-actual_qty-columns",
		"Stock Entry Detail-basic_rate-columns",
		"Purchase Order Item-schedule_date-columns",
		"Purchase Order Item-actual_qty-in_list_view",
		"Purchase Order Item-actual_qty-columns",
		"Purchase Order Item-warehouse-in_list_view",
		"Purchase Receipt Item-rate-columns",
		"Purchase Receipt Item-batch_no-columns",
		"Purchase Receipt Item-item_code-columns",
		"Purchase Receipt Item-net_amount-in_list_view",
		"Purchase Receipt Item-warehouse-in_list_view",
		"Purchase Receipt Item-serial_no-in_list_view",
		"Purchase Invoice Item-batch_no-in_list_view",
		"Purchase Invoice Item-batch_no-columns",
		"Purchase Invoice Item-rate-columns",
		"Sales Invoice Item-qty-columns",
		"Sales Invoice Item-income_account-in_list_view",
		"Sales Invoice Item-income_account-columns",
		"Sales Invoice Item-actual_qty-in_list_view",
		"Sales Invoice Item-actual_qty-columns",
		"Sales Invoice Item-item_code-columns",
		"Sales Invoice Item-warehouse-in_list_view",
		"Sales Invoice Item-batch_no-in_list_view",
		"Sales Invoice Item-serial_no-in_list_view",
		"Journal Entry Account-reference_type-in_list_view",
		"Journal Entry Account-debit_in_account_currency-columns",
		"Journal Entry Account-credit_in_account_currency-columns",
		"Journal Entry Account-party_type-columns",
		"Purchase Invoice Item-expense_account-in_list_view",
		"Purchase Invoice Item-item_code-columns",
		"Purchase Invoice Item-qty-columns",
		"Purchase Invoice Item-expense_account-columns",
		"Journal Entry Account-reference_type-columns",
		"Journal Entry Account-reference_name-columns",
		"Asset Finance Book-rate_of_depreciation-in_list_view",
		"Asset Finance Book-rate_of_depreciation-columns",
		"Asset Finance Book-total_number_of_depreciations-columns",
		"Production Plan-sub_assembly_items-allow_bulk_edit",
		"Production Plan-project-depends_on",
		"Purchase Receipt Item Supplied-consumed_qty-read_only_depends_on",
		"Training Result-employees-depends_on",	
		"Training Event-employees-depends_on"	
		]
	]
]
},
{"dt": "Client Script",
		"filters": [
         [
             "name", "in", [
		"POS Invoice-Form",
		"Item-Form",
		"Delivery Note-Form",
		"Item Attribute-Form",
		"Sales Invoice-Form",
		"Packing Slip-Form",
		"Sales Order-Form",
		"Stock Entry-Form",
		"Stock Reconciliation-Form"
		"Material Request-Form",
		"Pick List-Form",
		"Purchase Order-Form",
		"Purchase Invoice-Form",
		"Purchase Receipt-Form",
		"Payment Order-Form",
		"Payment Entry-Form",
		"Payment Request-Form",
		"Collection Details-List",
		"Style Details-List",
		"Launch Details-List",
		"Collection Details-Form",
		"Quality Inspection-Form",
		"Project-Form",
		"Material Request-Form",
		"Production Plan-Form",
		"Routing-Form",
		"Training Feedback-Form",
		"Training Result-Form",
		"Location-Form"
		]
	]
]
},
{"dt": "Print Format",
		"filters": [
         [
             "name", "in", [
		"Stock Reconciliation Barcode",
		"Stock Entry Barcode",
		"Item Barcode",
		"Domestic Sales Invoice",
		"Rangsutra Packing Slip",
		"Rangsutra POS Invoice Print Format",
		"Rangsutra Delivery Note Print Format",
		"Rangsutra Purchase Order Print Format",
		"Rangsutra Purchase Receipt Print Format",
		"Rangsutra Goods Return Challan Print Format",
		"Rangsutra Debit Note Print Format",
		"Domestic Credit Note",
		"Export Sales Invoice",
		"Rangsutra Delivery Note Return Print Format",
		"Export Credit Note",
		"Rangsutra Packing Slip Print Format",
		"Rangsutra Stock Entry Print Format",
		"Project Sales Invoice",
		"Shopify Sales Invoice",
		"Retail (Other) Sales Invoice"
		]
	]
]
},
{"dt": "Notification", 
		"filters": [
			"is_standard != 1"]
},
{"dt": "Report",
		"filters": [
         [
             "name", "in", [
		"Sales Order Item-wise Stock Report",
		"New Collections Sell Through Report",
		"Item-wise Sales Register With GST State Name",
		"Item-wise Purchase Register With GST State Name",
		"Sales Register With GST State Name"
		]
	]
]
},
{"dt": "Role", 
		"filters":[
        [
        "name","in",["Operations Manager - Retail",
			"Retail Merchandiser",
			"Retail Design & Business Manager",
			"Inventory & Retail Accounts Manager",
			"Stock Controller and Logistics In-Charge",
			"Store + RS Online Manager",
			"Marketing & Communications Executive",
			"Design Executive",
			"Digital Marketing and E-commerce Consultant",
			"Technical Support and Troubleshooting",
			"ERP User",
			"Quality User"
	]
	]
	]
},
{"dt": "Email Template",
		"filters":[
		[
		"name","in",["Purchase Receipt Template","Material Request Template","Purchase_receipt_QC_template","Blanket Order Template","In house QC Template","Email to Manufacturing Manager"
		]
		]
		]
},
{
    "dt":"Workspace",
    "filters":[
        [
        "name","in",[
		"Manufacturing"
        ]
    ]
]
}
]
doctype_js = {
	"Stock Entry" : "rangsutra/doctype/stock_entry/stock_entry.js"
}
override_doctype_dashboards = {
	"Purchase Order": "rangsutra.rangsutra.doctype.purchase_order.purchase_order_dashboard.get_dashboard_data",
	"Work Order": "rangsutra.rangsutra.doctype.work_order.work_order_dashboard.get_dashboard_data",
	"Project": "rangsutra.rangsutra.doctype.project.project_dashboard.get_dashboard_data"
}


# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/rangsutra/css/rangsutra.css"
# app_include_js = "/assets/rangsutra/js/rangsutra.js"

# include js, css files in header of web template
# web_include_css = "/assets/rangsutra/css/rangsutra.css"
# web_include_js = "/assets/rangsutra/js/rangsutra.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "rangsutra/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "rangsutra.install.before_install"
# after_install = "rangsutra.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "rangsutra.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

override_doctype_class = {	
	"Training Feedback": "rangsutra.rangsutra.doctype.training_feedback.training_feedback.CustomTrainingFeedback"	
}

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"rangsutra.tasks.all"
# 	],
# 	"daily": [
# 		"rangsutra.tasks.daily"
# 	],
# 	"hourly": [
# 		"rangsutra.tasks.hourly"
# 	],
# 	"weekly": [
# 		"rangsutra.tasks.weekly"
# 	]
# 	"monthly": [
# 		"rangsutra.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "rangsutra.install.before_tests"

# Overriding Methods
# ------------------------------
#
#override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "rangsutra.event.get_events"
#	"frappe.contacts.doctype.address.address.get_default_address": "rangsutra.rangsutra.contacts.doctype.address.address.get_default_address"
#}
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "rangsutra.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

