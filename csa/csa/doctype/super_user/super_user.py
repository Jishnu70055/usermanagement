# Copyright (c) 2021, s and contributors
# For license information, please see license.txt
import re
from datetime import date
from datetime import datetime
import frappe
from frappe.model.document import Document
import random
class SuperUser(Document):
	def before_save(self):
		if self.password == self.re_enter_password:
			if len(self.password) >= 10:
				if re.search(r"[A-Z]", self.password):
					if re.search(r"[a-z]", self.password):
						if re.search(r"[ @!#$%&?'()*+,-./[\\\]^_`{|}~"+r'"]', self.password):
							if re.search("[0-9]", self.password):
								user = frappe.new_doc('User')
								user.email = self.email_id
								user.first_name = self.first_name
								user.last_name = self.last_name
								user.username = self.user_name
								user.save(ignore_permissions=True)
								user_modifiy = frappe.get_doc('User' ,user.name)
								user_modifiy.update({
									"doctype":"User",
									"new_password" : self.password,
									"logout_all_sessions":1
								})
								user_modifiy.append('roles',{
											"doctype": "Has Role",
											"role":"Super User"
											})
								user_modifiy.save(ignore_permissions=True)
								
							else:
								frappe.throw('Password Must Contain Uppercase,Lowecase,Numbers,Characters and Length More Than 10')
						else:
							frappe.throw('Password Must Contain Uppercase,Lowecase,Numbers,Characters and Length More Than 10')

					else:
						frappe.throw('Password Must Contain Uppercase,Lowecase,Numbers,Characters and Length More Than 10')
				else:
					frappe.throw('Password Must Contain Uppercase,Lowecase,Numbers,Characters and Length More Than 10')
			else:
				frappe.throw('Password Must Contain Uppercase,Lowecase,Numbers,Characters and Length More Than 10')
		else:
			frappe.throw('Password Not Matching')
	





def random_number():
	num = '1234567890'
	ref = ''.join(random.sample(num,1))
	random_num = ref 
	return random_num