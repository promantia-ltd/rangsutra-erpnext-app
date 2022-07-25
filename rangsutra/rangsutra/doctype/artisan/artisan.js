// Copyright (c) 2022, rangsutra_app and contributors
// For license information, please see license.txt

frappe.ui.form.on('Artisan', {
    refresh(frm) {
        frm.set_query("reports_to", function() {
            return {
                filters: {
                    "is_craft_manager": 1
                }
            };
        });

        frm.add_custom_button(__("Training History"), function() {
            frappe.route_options = {
                is_artisan_training: 1,
                artisan: frm.doc.name
            };
            frappe.set_route('Form', 'Training Event');
        }, __("View"));

    },
    date_of_birth: function(frm) {
        let today = new Date();
        let birthDate = new Date(frm.doc.date_of_birth);
        let age = today.getFullYear() - birthDate.getFullYear();
        frm.set_value('age', age);
    },
    is_craft_manager: function(frm) {
        if (frm.doc.is_craft_manager == 1) {
            frm.set_value('designation', 'Craft Manager');
        } else {
            frm.set_value('designation', '');
        }
    }
});