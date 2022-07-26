// Copyright (c) 2022, rangsutra_app and contributors
// For license information, please see license.txt

frappe.ui.form.on('Craft Order', {
    onload: function(frm) {
        if (frm.doc.purchase_order != undefined && frm.doc.__islocal) {
            frappe.model.with_doc("Purchase Order", frm.doc.purchase_order, function() {
                var tabletransfer = frappe.model.get_doc("Purchase Order", frm.doc.purchase_order)
                $.each(tabletransfer.items, function(index, row) {
                    var d = frm.add_child("items");
                    d.subcontracted_item_code = row.item_code;
                    d.subcontracted_item_name = row.item_name;
                    d.total_qty = row.qty;
                    frm.refresh_field("items");
                });
                $.each(tabletransfer.supplied_items, function(index, line) {
                    var remaining_issue_qty = 0;

                    var a = frm.add_child("raw_materials_issued");
                    a.subcontracted_item_code = line.main_item_code;
                    a.raw_materials_issue_item_code = line.rm_item_code;
                    a.total_issue_qty = line.required_qty;
                    frm.call({
                        method: 'rangsutra.rangsutra.doctype.craft_order.craft_order.get_remaining_issue_qty',
                        args: {
                            subcontracted_item_code: line.main_item_code,
                            raw_materials_issue_item_code: line.rm_item_code,
                            purchase_order: frm.doc.purchase_order
                        },
                        callback: function(r) {
                            remaining_issue_qty = line.required_qty - r.message;
                            if (remaining_issue_qty >= 0) {
                                a.issued_qty = remaining_issue_qty;
                            } else {
                                a.issued_qty = 0;
                            }
                            frm.refresh_field("raw_materials_issued");
                        }
                    });

                    frm.refresh_field("raw_materials_issued");
                });
            });
        }
    },
    refresh: function(frm) {
        frm.set_query("craft_manager", function() {
            return {
                filters: {
                    "is_craft_manager": 1
                }
            };
        });
    }
});