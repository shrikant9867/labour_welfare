// Copyright (c) 2021, Sumit and contributors
// For license information, please see license.txt

frappe.ui.form.on('Labour Welfare Board', {
	validate: function (frm) {
		frm.set_value("registation_no", frm.doc.registration_number_search)
	}
});