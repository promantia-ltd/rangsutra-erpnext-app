frappe.ui.form.on('Stock Entry', {
refresh: function(frm){
    if (frm.doc.docstatus === 1) {
        frm.add_custom_button(__('E-Way Bill JSON'), function () {
            frappe.call({
                method: 'rangsutra.rangsutra.doctype.stock_entry.stock_entry.generate_ewaybill_json',
                args: {
                    'dt': frm.doc.doctype,
                    'dn': frm.doc.name
                },
                callback: function(r) {
                    if (r.message) {
                        const args = {
                            cmd: 'erpnext.regional.india.utils.download_ewb_json',
                            data: r.message,
                            docname: frm.doc.name
                        };
                        open_url_post(frappe.request.url, args);
                    }
                }
            });
        }, __('Create'));
    }
    if (frm.doc.stock_entry_type == 'Send to Subcontractor') {
        frappe.db.get_value("Purchase Order", frm.doc.purchase_order, "supplier",(s)=>{
            console.log(s.supplier);
            frm.set_value("suppliers_name", s.supplier)
        });
    }
},
suppliers_name: function (frm) {

    frm.set_query("suppliers_address", function(doc) {
        return {
            filters: {
                "link_doctype": "Supplier",
                "link_name": doc.suppliers_name
            }
        };
    });
},
suppliers_address: function(frm) {
    if (frm.doc.suppliers_address) {
        frappe.call({
            method: 'frappe.contacts.doctype.address.address.get_address_display',
            args: {
                "address_dict": frm.doc.suppliers_address
            },
            callback: function(r) {
                frm.set_value("suppliers_address_details", r.message);
            }
        });
    }
    if (!frm.doc.suppliers_address) {
        frm.set_value("suppliers_address_details", "");
    }
}
});