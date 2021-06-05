// Copyright (c) 2021, Sumit and contributors
// For license information, please see license.txt

frappe.ui.form.on('Labour Welfare Board', {
	refresh: function (frm) {
		
	},
	onload: function (frm)
	registration_number: function(frm){
		console.log("FunctionCalled.");
		frappe.call({
			method:'labour_welfare.labour_welfare.doctype.labour_welfare_board.labour_welfare_board.get_registration_data',
			args:{
				"registration_id":frm.doc.registration_number
			},
			callback:function(r){
				console.log(r.message[0]);
				if (r.message[0]){
					console.log(r.message[0].registration_date);
					//frm.doc.registration_date = r.message[0].registration_date;
					//frm.set_value("registration_date",r.message[0].registration_date);
					set_form_values(frm,r.message[0]); 
				}
			}
	});
		console.log("TPPPPPPPPPPPFunctionCalled.",);
}
});
var set_form_values = function(frm,data){
		frm.set_value("registration_date",data.registration_date);
};