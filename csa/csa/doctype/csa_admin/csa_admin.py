# Copyright (c) 2021, s and contributors
# For license information, please see license.txt
from datetime import date
from datetime import datetime
import frappe
from frappe.model.document import Document
import random


class CSAAdmin(Document):
	def before_save(self):
		first_name = str(self.first_name[0])
		last_name = str(self.last_name [0])
		date_stamp = self.date_of_birth
		dob = datetime.strptime(date_stamp, '%Y-%m-%d')
		month = str(dob.strftime('%m'))
		day = str(dob.strftime('%d'))
		year = str(dob.strftime('%y'))
		# month = str(dob.month)
		# day = str(dob.day)
		# year = str(dob.year)
		id = first_name+last_name+year+month+day
		if self.gender == 'Male':
			name = str(id)+str(random_number_males())
			self.user_name = name
			user_creation(self)
			# frappe.throw(self.user_name)
		if self.gender == 'Female':
			self.user_name = str(id) + str(random_number_females())
			user_creation(self)
			# frappe.throw(self.user_name)
		if self.gender == 'Others':
			self.user_name = str(id) + str(random_number_others())
			user_creation(self)
	


		# user_modifiy.set_new_password = self.mobile_number
		# frappe.throw(user_modifiy.set_new_password)
		# user_modifiy.sales_user = 1
		
def user_creation(self):
	user = frappe.new_doc('User')
	user.email = self.email_id
	user.first_name = self.first_name
	user.last_name = self.last_name
	user.username = self.user_name
	user.save(ignore_permissions=True)
	user_modifiy = frappe.get_doc('User' ,user.name)
	user_modifiy.update({
		"doctype":"User",
		"logout_all_sessions":1
	})
	user_modifiy.append('roles',{
				"doctype": "Has Role",
				"role":"Sales User"
				})
	user_modifiy.save(ignore_permissions=True)


def random_number_males():
	for rand_num in [random.randrange(*sorted([4000,8999])) for i in range(10)]:
		return rand_num


def random_number_females():
	for rand_num in [random.randrange(*sorted([0,3999])) for i in range(10)]:
		return rand_num


def random_number_others():
	for rand_num in [random.randrange(*sorted([9000,9999])) for i in range(10)]:
		return rand_num


	# num = '1234567890'
	# ref = ''.join(random.sample(num,1))
	# random_num = ref 
	# return random_num