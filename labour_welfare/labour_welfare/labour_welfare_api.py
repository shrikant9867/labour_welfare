from __future__ import unicode_literals
import frappe
import time
from frappe.utils import flt, now_datetime, cstr, add_to_date, date_diff, nowdate, add_days, getdate
from frappe import _
import requests
import json 
import tempfile
from datetime import datetime



@frappe.whitelist()
def labour_welfare(data=None):
	data = json.loads(data)
	if data.get("name"):
		labour_data = frappe.db.sql("""SELECT * from `tabLabour Welfare Board` where name='{0}'""".format(data.get("name")), as_dict=1, debug=1)
		return labour_data
	elif frappe.db.get_value("Labour Welfare Board", data.get("registration_number")):
		doc = frappe.get_doc("Labour Welfare Board", data.get("registration_number"))
		doc.registration_number_search = data.get("registration_number")
		doc.new_form = False
		doc.renewal = True
		doc.registration_date = getdate(data.get("registration_date"))
		doc.full_name_of_domestic_work = data.get("full_name_worker")
		doc.birthdate_of_beneficiany = getdate(data.get("birthdate_of_baneficiary"))
		doc.age_of_beneficiary = data.get("age")
		doc.mobile_number = data.get("mobile_number")
		if data.get("sex")=="male":
			doc.sex="Male / पुरूष"
		elif data.get("sex")=="female":
			doc.sex="Female / महिला"
		else:
			doc.sex="Other / इतर"
		doc.adhar_card_number=data.get("adhar_card_number")
		doc.residence_address=data.get("residence_address")
		doc.district=data.get("district")
		doc.village_city=data.get("village_city")
		doc.pincode=data.get("pincode")
		doc.owner_name=data.get("owner_name")
		doc.owner_mobile_number=data.get("owner_mobile_number")
		doc.owner_address=data.get("owner_address")
		doc.beneficiary_bank_name=data.get("bank_name")
		doc.beneficiary_bank_account_number=data.get("bank_account_number")
		doc.ifsc_code=data.get("ifsc_code")
		doc.beneficiaries_total_number_of_offspring=data.get("child_qty")
		doc.name_of_nominee=data.get("name_of_nominee")
		doc.relationship_to_nominee=data.get("relationship_name")
		doc.receipt_image_file_name=data.get("receipt_file_name")
		doc.identity_proof_file_name=data.get("adhar_card_copy")
		doc.bank_copy_file_name=data.get("bank_pass_copy")
		doc.address_proof_file_name=data.get("residential_proof")
		doc.please_choose_any_one_identity_proof=data.get("photo_id")
		doc.please_choose_any_one_address_proof = data.get("address_proof")
		doc.please_select_an_option=data.get("bank_copy")
		doc.registration_district=data.get("registration_district")
		doc.welfare_id = data.get("welfare_id")
		doc.last_modified_date = now_datetime()
		doc.house_number = data.get("house_nunmber")
		doc.post_office = data.get("post_office")
		doc.save()
		frappe.db.commit()
	else:
		doc = frappe.new_doc("Labour Welfare Board")
		doc.registation_no = data.get("registration_number")
		doc.registration_number_search = data.get("registration_number")
		doc.new_form = True
		doc.renewal = False
		doc.registration_date = getdate(data.get("registration_date"))
		doc.full_name_of_domestic_work = data.get("full_name_worker")
		doc.birthdate_of_beneficiany = getdate(data.get("birthdate_of_baneficiary"))
		doc.age_of_beneficiary = data.get("age")
		doc.mobile_number = data.get("mobile_number")
		if data.get("sex")=="male":
			doc.sex="Male / पुरूष"
		elif data.get("sex")=="female":
			doc.sex="Female / महिला"
		else:
			doc.sex="Other / इतर"
		doc.adhar_card_number=data.get("adhar_card_number")
		doc.residence_address=data.get("residence_address")
		doc.district=data.get("district")
		doc.village_city=data.get("village_city")
		doc.pincode=data.get("pincode")
		doc.owner_name=data.get("owner_name")
		doc.owner_mobile_number=data.get("owner_mobile_number")
		doc.owner_address=data.get("owner_address")
		doc.beneficiary_bank_name=data.get("bank_name")
		doc.beneficiary_bank_account_number=data.get("bank_account_number")
		doc.ifsc_code=data.get("ifsc_code")
		doc.beneficiaries_total_number_of_offspring=data.get("child_qty")
		doc.name_of_nominee=data.get("name_of_nominee")
		doc.relationship_to_nominee=data.get("relationship_name")
		doc.receipt_image_file_name=data.get("receipt_file_name")
		doc.identity_proof_file_name=data.get("adhar_card_copy")
		doc.bank_copy_file_name=data.get("bank_pass_copy")
		doc.address_proof_file_name=data.get("residential_proof")
		doc.please_choose_any_one_identity_proof=data.get("photo_id")
		doc.please_choose_any_one_address_proof = data.get("address_proof")
		doc.please_select_an_option=data.get("bank_copy")
		doc.welfare_id = data.get("welfare_id")
		doc.registration_district=data.get("registration_district")
		doc.last_modified_date = now_datetime()
		doc.house_number = data.get("house_nunmber")
		doc.post_office = data.get("post_office")
		doc.save()
		frappe.db.commit()

	filename = []
	file_content = []
	filename.append(data.get("receipt_file_name"))
	filename.append(data.get("adhar_card_copy"))
	# filename.append(data.get("residential_proof"))
	filename.append(data.get("bank_pass_copy"))

	file_content.append(data.get("receipt_file_content"))
	file_content.append(data.get("adhar_card_content"))
	# file_content.append(data.get("residential_proof_content"))
	file_content.append(data.get("bank_pass_content"))

	for idx, row in enumerate(file_content):
		new_image = bytes(row,'utf-8')
		_file = frappe.get_doc({
			"doctype": "File",
			"file_name": filename[idx],
			"attached_to_doctype": "Labour Welfare Board",
			"attached_to_name": data.get("registration_number"),
			"is_private": 0,
			"content": new_image,
			"decode": 1})
		_file.save()


@frappe.whitelist()
def bank_name_data():
	bank_name = frappe.db.sql("""SELECT name From `tabBank Name` ORDER BY name asc""", as_list=1)
	return bank_name

@frappe.whitelist()
def registration_districts():
	registration_districts = frappe.db.sql("""SELECT name From `tabRegistration Districts` ORDER BY name asc""", as_list=1)
	return registration_districts

@frappe.whitelist()
def district():
	district = frappe.db.sql("""SELECT name From `tabDistrict` ORDER BY name asc""", as_list=1)
	return district