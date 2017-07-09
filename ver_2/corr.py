class Corrector(object):
	'''Parse input string'''
	
	new_str = ""

	def __init__(self, my_str):
		self.new_str = my_str
	
	def del_spaces(self):
		self.new_str = self.new_str.replace(" ", "")
		return self.new_str
	
	def check_signs(self):
		final_str = False
		while not final_str:
			final_str = True
			if "++" in self.new_str:
				final_str = False
				self.new_str = self.new_str.replace("++", "+")
			elif "--" in self.new_str:
				final_str = False
				self.new_str = self.new_str.replace("--", "+")
			elif "+-" in self.new_str:
				final_str = False
				self.new_str = self.new_str.replace("+-", "-")
			elif "-+" in self.new_str:
				final_str = False
				self.new_str = self.new_str.replace("-+", "-")
		return self.new_str
	
	def support_oper(self):
		support_symb = "+-*/%."
		for i in range(len(self.new_str)):
			if self.new_str[i].isdigit():
				pass
			elif self.new_str[i] not in support_symb:
				print("Unsupport operation - {0}".format(self.new_str[i]))
				return TypeError
			

	def output_str(self):
		return self.new_str
