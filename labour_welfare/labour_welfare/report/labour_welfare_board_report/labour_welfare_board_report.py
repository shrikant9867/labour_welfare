# Copyright (c) 2013, Bakelite and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import has_common
import json
from six import StringIO, string_types
from datetime import date
from frappe.utils import cstr, getdate, split_emails, add_days, today, get_last_day, get_first_day, month_diff, nowdate

def execute(filters=None):
	columns, data = get_columns(), get_data(filters)
	return columns, data
	
def get_data(filters):
	user = frappe.session.user

	query_data = frappe.db.sql(""" SELECT registration_number_search, registration_date, last_modified_date, registration_district, full_name_of_domestic_work, birthdate_of_beneficiany, age_of_beneficiary, sex, mobile_number, adhar_card_number, residence_address, state, district, village_city, pincode, owner_name, owner_address, owner_mobile_number, beneficiary_bank_name, beneficiary_bank_name, beneficiary_bank_account_number, ifsc_code, beneficiaries_total_number_of_offspring, name_of_nominee, relationship_to_nominee, welfare_id, receipt_image_file_name, please_choose_any_one_identity_proof, identity_proof_file_name, please_choose_any_one_address_proof, address_proof_file_name, please_select_an_option, bank_copy_file_name from `tabLabour Welfare Board` where {0}""".format(get_filters_codition(filters)),as_dict=True, debug=1)
   
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
			"label": _("Registration Date"),
			"fieldname": "registration_date",
			"fieldtype": "Date",
			"width": 120
		},
		{
			"label": _("Last Modified Date"),
			"fieldname": "last_modified_date",
			"fieldtype": "Date",
			"width": 120
		},
		{
			"label": _("Registration District"),
			"fieldname": "registration_district",
			"fieldtype": "Link",
			"options": "Registration Districts",
			"width": 120
		},
		{
			"label": _("Full Name of Domestic Work"),
			"fieldname": "full_name_of_domestic_work",
			"fieldtype": "Data",
			"width": 150
		},
		{
			"label": _("Birthdate of Beneficiany"),
			"fieldname": "birthdate_of_beneficiany",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Age of Beneficiary"),
			"fieldname": "age_of_beneficiary",
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
			"label": _("Mobile Number"),
			"fieldname": "mobile_number",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Adhar Card Number"),
			"fieldname": "adhar_card_number",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Residence Address"),
			"fieldname": "residence_address",
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
			"label": _("District"),
			"fieldname": "district",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Village/City"),
			"fieldname": "village_city",
			"fieldtype": "Data",
			"width": 150
		},
		{
			"label": _("Pincode"),
			"fieldname": "pincode",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Employer Name"),
			"fieldname": "owner_name",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Employer Address"),
			"fieldname": "owner_address",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Employer Mobile Number"),
			"fieldname": "owner_mobile_number",
			"fieldtype": "Data",
			"width": 150
		},
		{
			"label": _("Beneficiary Bank Name"),
			"fieldname": "beneficiary_bank_name",
			"fieldtype": "Data",
			"width": 150
		},
		{
			"label": _("Beneficiary Bank Account Number"),
			"fieldname": "beneficiary_bank_account_number",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("IFSC Code"),
			"fieldname": "ifsc_code",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Beneficiaries Total number of offspring"),
			"fieldname": "beneficiaries_total_number_of_offspring",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Name Of Nominee"),
			"fieldname": "name_of_nominee",
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
			"label": _("Adhar Card Number"),
			"fieldname": "adhar_card_number",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Residence Address"),
			"fieldname": "residence_address",
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
			"label": _("District"),
			"fieldname": "district",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Village/City"),
			"fieldname": "village_city",
			"fieldtype": "Data",
			"width": 150
		},
		{
			"label": _("Pincode"),
			"fieldname": "pincode",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Employer Name"),
			"fieldname": "owner_name",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Employer Address"),
			"fieldname": "owner_address",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Employer Mobile Number"),
			"fieldname": "owner_mobile_number",
			"fieldtype": "Data",
			"width": 150
		},
		{
			"label": _("Beneficiary Bank Name"),
			"fieldname": "beneficiary_bank_name",
			"fieldtype": "Data",
			"width": 150
		},
		{
			"label": _("Beneficiary Bank Account Number"),
			"fieldname": "beneficiary_bank_account_number",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("IFSC Code"),
			"fieldname": "ifsc_code",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Beneficiaries Total number of offspring"),
			"fieldname": "beneficiaries_total_number_of_offspring",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Name Of Nominee"),
			"fieldname": "name_of_nominee",
			"fieldtype": "Data",
			"width": 150
		},
		{
			"label": _("Relationship to Nominee"),
			"fieldname": "relationship_to_nominee",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Please Choose Any One  Labour Welfare Identity Card/Receipt Name"),
			"fieldname": "welfare_id",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Receipt Image File Name"),
			"fieldname": "receipt_image_file_name",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Please Choose Any One Identity Proof"),
			"fieldname": "please_choose_any_one_identity_proof",
			"fieldtype": "Data",
			"width": 150
		},
		{
			"label": _("Identity Proof File Name"),
			"fieldname": "identity_proof_file_name",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Please Choose Any One Address Proof"),
			"fieldname": "please_choose_any_one_address_proof",
			"fieldtype": "Data",
			"width": 150
		},
		{
			"label": _("Please Select An Option"),
			"fieldname": "address_proof_file_name",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Please Select An Option"),
			"fieldname": "please_select_an_option",
			"fieldtype": "Data",
			"width": 120
		},
		{
			"label": _("Bank Copy File Name"),
			"fieldname": "bank_copy_file_name",
			"fieldtype": "Data",
			"width": 120
		}
	]