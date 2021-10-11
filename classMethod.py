class Employee():

	raise_amout = 10
	num_of_emps= 0
	def __init__(self, fname,lname,salary): #constructor 
		self.fname = fname
		self.lname = lname
		self.salary = salary
		self.email = fname + "." + lname + "@email.com"
		Employee.num_of_emps+= 1

	def displaydata(self):
		return '{} {} {} {}'.format(self.fname, self.lname, self.salary, self.email)

	def applyraise(self):
		self.salary = int(self.salary * self.raise_amout)

	@classmethod
	def set_raise_amt(cls, amount): 
		cls.raise_amout = amount


	@classmethod
	def date(cls,emp_str):



e1 = Employee('Sayaji','Chavan',120000)
e2 = Employee('Nilesh','Bhise',120000)


Employee.set_raise_amt(12)

print(Employee.raise_amout)
print(e1.raise_amout)
print(e2.raise_amout)
print(Employee.num_of_emps)



#class variable are variales declared inside 