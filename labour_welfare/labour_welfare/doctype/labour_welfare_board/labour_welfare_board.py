# Copyright (c) 2021, Sumit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class LabourWelfareBoard(Document):
	pass


@frappe.whitelist()
def get_registration_data(registration_id):
	data = frappe.db.sql(""" select * from `tabLabour Welfare Board` where registration_number = '{}'""".format(registration_id),as_dict = 1)
	print(data,"\n\n\n\n\n\n\n")
	return data
