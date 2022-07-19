// Copyright (c) 2022, rangsutra_app and contributors
// For license information, please see license.txt

frappe.ui.form.on('Artisan', {
	date_of_birth: function(frm) {
		let today = new Date();
		let birthDate = new Date(frm.doc.date_of_birth); 
		let age = today.getFullYear() - birthDate.getFullYear();
		frm.set_value('age', age);
	},
	refresh(frm) {
		frm.set_query("reports_to",function(){
			return{
				filters: {
					"is_craft_manager":1
				}
			};
		});
	}
});