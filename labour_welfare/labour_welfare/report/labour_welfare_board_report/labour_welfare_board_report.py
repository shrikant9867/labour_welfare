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

	query_data = frappe.db.sql(""" SELECT name from `tabLabour Welfare Board` limit 10""".format(),as_dict=True, debug=1)
   
	return query_data

# def get_filters_codition(filters):
# 	conditions = "1=1"
# 	if filters.get("student_email_id"):
# 		conditions += " and name = '{0}'".format(filters.get('student_email_id'))
# 	if filters.get("from_date"):
# 		conditions += " and creation >= '{0}'".format(filters.get('from_date'))
# 	if filters.get("to_date"):
# 		conditions += " and creation <= '{0}'".format(filters.get('to_date'))
# 	return conditions

def get_columns():
	return	[
		{
			"label": _("Name"),
			"fieldname": "name",
			"fieldtype": "Data",
			"width": 150
		}
		# {
		# 	"label": _("Date"),
		# 	"fieldname": "creation",
		# 	"fieldtype": "Date",
		# 	"width": 120
		# },
		# {
		# 	"label": _("Student Roll Number"),
		# 	"fieldname": "student_roll_number",
		# 	"fieldtype": "Data",
		# 	"width": 120
		# },
		# {
		# 	"label": _("Student Email Id"),
		# 	"fieldname": "student_email_id",
		# 	"fieldtype": "Data",
		# 	"width": 150
		# },
		# {
		# 	"label": _("Tenure"),
		# 	"fieldname": "tenure",
		# 	"fieldtype": "Data",
		# 	"width": 120
		# },
		# {
		# 	"label": _("Joining Date"),
		# 	"fieldname": "joining_date",
		# 	"fieldtype": "Date",
		# 	"width": 120
		# },
		# {
		# 	"label": _("Course"),
		# 	"fieldname": "course",
		# 	"options":"Course",
		# 	"fieldtype": "Link",
		# 	"width": 150
		# },
		# {
		# 	"label": _("Payment Type"),
		# 	"fieldname": "payment_method",
		# 	"fieldtype": "Data",
		# 	"width": 120
		# },
		# {
		# 	"label": _("Payment Method"),
		# 	"fieldname": "payment_type",
		# 	"fieldtype": "Data",
		# 	"width": 120
		# },
		# {
		# 	"label": _("Status"),
		# 	"fieldname": "status",
		# 	"fieldtype": "Data",
		# 	"width": 120
		# },
		# {
		# 	"label": _("Payment Pending Days"),
		# 	"fieldname": "payment_pending_days",
		# 	"fieldtype": "Data",
		# 	"width": 150
		# }
	]