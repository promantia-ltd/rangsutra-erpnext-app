// Copyright (c) 2022, rangsutra_app and contributors
// For license information, please see license.txt

frappe.ui.form.on('Variant BOM Generator', {
    refresh: function(frm) {
        frm.set_query("finished_good_item", function() {
            return {
                filters: {
                    "is_finished_product": 1,
                    "has_variants": 1
                }
            };
        });
        frm.set_query("item_code", "raw_materials", function() {
            return {
                query: "rangsutra.rangsutra.doctype.variant_bom_generator.variant_bom_generator.get_item_filter",
                filters: {}
            };
        });
        frm.set_query("associated_intermediate_item", function() {
            return {
                filters: {
                    "intermediate_product": 1,
                    "has_variants": 1
                }
            };
        });
        var operations = [];
        frm.call({
            'doc': frm.doc,
            method: "get_operations",
            callback: function(r) {
                for (var i = 0; i < r.message.length; i++) {
                    operations.push(r.message[i].operation);
                }
            }
        })
        frm.set_query("operation", "raw_materials", function() {
            return {
                filters: {
                    "name": ["in", operations]
                }
            };
        });
    },
    generate_bom(frm) {
        frm.call({
            'doc': frm.doc,
            method: 'get_variant_items',
            callback: function(r) {
                if (!r.message) {
                    frappe.msgprint({
                        title: __('Variant BOM not created'),
                        message: __('No Variant Items available for the finished good'),
                        indicator: 'orange'
                    });
                    return;
                } else {
                    const fields = [{
                        label: 'Items',
                        fieldtype: 'Table',
                        fieldname: 'items',
                        fields: [{
                            fieldtype: 'Read Only',
                            fieldname: 'item_code',
                            label: __('Item Code'),
                            in_list_view: 1
                        }, {
                            fieldtype: 'Read Only',
                            fieldname: 'item_name',
                            label: __('Item Name'),
                            in_list_view: 1
                        }],
                        data: r.message,
                        get_data: () => {
                            return r.message
                        }
                    }]
                    var d = new frappe.ui.Dialog({
                        title: __('Select Items to generate BOM'),
                        fields: fields,
                        primary_action: function() {
                            var data = { items: d.fields_dict.items.grid.get_selected_children() };

                            frm.call({
                                method: 'rangsutra.rangsutra.doctype.variant_bom_generator.variant_bom_generator.generate_variant_template_bom',
                                args: {
                                    doc: frm.doc,
                                    items: data
                                },
                                freeze: true,
                                callback: function(r) {
                                    frm.reload_doc();
                                    d.hide();
                                }
                            });
                        },
                        primary_action_label: __('Create')
                    });
                    d.show();
                }
            }
        })
    }
});