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



fixtures = [
{
    "dt":"DocType",
    "filters":[
        [
        "name","in",[
		"Style Details",
		"Collection Details",
		"Launch Details"
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
		"Item-updated_item"
		]
	]
]
},
{"dt": "Custom Script",
		"filters": [
         [
             "name", "in", [
		"POS Invoice-Client",
		"Item-Client"
		]
	]
]
},
{"dt": "Server Script",
		"filters": [
         [
             "name", "in", [
		"item_codification"
		]
	]
]
}
]
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

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

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
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "rangsutra.event.get_events"
# }
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

