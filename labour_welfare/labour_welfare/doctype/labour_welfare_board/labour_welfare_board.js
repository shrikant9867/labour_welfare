// Copyright (c) 2021, Sumit and contributors
// For license information, please see license.txt

frappe.ui.form.on('Labour Welfare Board', {
	refresh: function (frm) {
		
	},
	onload: function (frm) {
		if(frm.doc.dob){
			$(frm.fields_dict['age_of_beneficiary'].wrapper).html("AGE : " + get_age(frm.doc.dob));
		}
	}
});

frappe.ui.form.on("Labour Welfare Board", "dob", function(frm) {
	if(frm.doc.dob){
		var today = new Date();
		var birthDate = new Date(frm.doc.dob);
		var age_str = get_age(frm.doc.dob);
		$(frm.fields_dict['age_of_beneficiary'].wrapper).html("AGE : " + age_str);
	}
});

var get_age = function (birth) {
	var ageMS = Date.parse(Date()) - Date.parse(birth);
	var age_of_beneficiary = new Date();
	age_of_beneficiary.setTime(ageMS);
	var years = age_of_beneficiary.getFullYear() - 1970;
	return years + " Year(s) " + age_of_beneficiary.getMonth() + " Month(s) " + age_of_beneficiary.getDate() + " Day(s)";
};