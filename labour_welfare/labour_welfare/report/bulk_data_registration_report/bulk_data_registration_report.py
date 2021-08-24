# Copyright (c) 2013, Sumit and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from datetime import date, datetime
from frappe.utils import cstr, getdate, split_emails, add_days, today, get_last_day, get_first_day, month_diff, nowdate

def execute(filters=None):
	columns, data = get_columns(), get_data(filters)
	return columns, data
	
def get_data(filters):
	user = frappe.session.user

	query_data = frappe.db.sql(""" SELECT registration_number_search, registration_date, last_modified_date, registration_district, full_name_of_domestic_work, birthdate_of_beneficiany, age_of_beneficiary, sex, mobile_number, adhar_card_number, residence_address, state, district, village_city, pincode, owner_name, owner_address, owner_mobile_number, beneficiary_bank_name, beneficiary_bank_name, beneficiary_bank_account_number, ifsc_code, beneficiaries_total_number_of_offspring, name_of_nominee, post_office, house_number from `tabLabour Welfare Board` where {0}""".format(get_filters_codition(filters)),as_dict=True, debug=1)
   
	return query_data

def get_filters_codition(filters):
	conditions = "1=1"
	if filters.get("registration_number_search"):
		conditions += " and registration_number_search = '{0}'".format(filters.get('registration_number_search'))

	if filters.get("registration_district"):
		conditions += " and registration_district = '{0}'".format(filters.get('registration_district'))

	if filters.get("district"):
		conditions += " and district = '{0}'".format(filters.get('district'))

	if filters.get("from_date"):
		conditions += " and registration_date >= '{0}'".format(filters.get('from_date'))
	if filters.get("to_date"):
		conditions += " and registration_date <= '{0}'".format(filters.get('to_date'))
	return conditions

def get_columns():
	return	[
		{
			"label": _("Registration Number"),
			"fieldname": "registration_number_search",
			"fieldtype": "Data",
			"width": 150
		},
		{
			"label": _("Full Name of Domestic Work"),
			"fieldname": "full_name_of_domestic_work",
			"fieldtype": "Data",
			"width": 150
		},
		{
			"label": _("Mobile Number"),
			"fieldname": "mobile_number",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Birthdate of Beneficiany"),
			"fieldname": "birthdate_of_beneficiany",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Sex"),
			"fieldname": "sex",
			"fieldtype": "Data",
			"width": 150
		},
		{
			"label": _("Adhar Card Number"),
			"fieldname": "adhar_card_number",
			"fieldtype": "Data",
			"width": 120
		},		
		{
			"label": _("State"),
			"fieldname": "state",
			"fieldtype": "Data",
			"width": 150
		},
		{
			"label": _("Residence District"),
			"fieldname": "district",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("House Number"),
			"fieldname": "house_number",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Village/Locality"),
			"fieldname": "village_city",
			"fieldtype": "Data",
			"width": 150
		},
		{
			"label": _("Post Office"),
			"fieldname": "post_office",
			"fieldtype": "Data",
			"width": 150
		},
		{
			"label": _("Pincode"),
			"fieldname": "pincode",
			"fieldtype": "Data",
			"width": 120
		}
	]