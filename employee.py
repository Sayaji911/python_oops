class Employee():
	def __init__(self, fname,lname,salary): #constructor 
		self.fname = fname
		self.lname = lname
		self.salary = salary
		self.email = fname + "." + lname + "@email.com"

	def displaydata(self):
		return '{} {} {} {}'.format(self.fname, self.lname, self.salary, self.email)
e1 = Employee('Sayaji','Chavan',120000)
e2 = Employee('Nilesh','Bhise',120000)

print(e2.fname)
print(e1.fname)
print("---------------------------------")

print(e1.displaydata())