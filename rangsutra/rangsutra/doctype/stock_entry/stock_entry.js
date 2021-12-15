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
}
});