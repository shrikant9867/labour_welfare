// Copyright (c) 2016, Sumit and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Bulk Data Registration Report"] = {
	"filters": [
		{
			"fieldname":"registration_number_search",
			"label": __("Registration Number"),
			"fieldtype": "Link",
			"options":'Labour Welfare Board'
		},
		{
			"fieldname":"registration_district",
			"label": __("Registration District"),
			"fieldtype": "Link",
			"options":'Registration Districts'
		},
		{
			"fieldname":"last_modified_date",
			"label": __("Last Modified Date"),
			"fieldtype": "Date"
		},
		{
			"fieldname":"district",
			"label": __("Residence District"),
			"fieldtype": "Link",
			"options":'District'
		},
		{
			"fieldname":"from_date",
			"label": __("From Date"),
			"fieldtype": "Date"
		},
		{
			"fieldname":"to_date",
			"label": __("To Date"),
			"fieldtype": "Date"
		}
		

	]
};
