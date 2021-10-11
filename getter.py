class Employee():
	def __init__(self, fname,lname,salary): #constructor 
		self.fname = fname
		self.lname = lname
		self.salary = salary

	def displaydata(self):
		return '{} {} {} {}'.format(self.fname, self.lname, self.salary, self.email)


	@property
	def fullname(self):
		return '{} {}'.format(self.fname, self.lname)

	@property #use function as propertyyyy 
	def email(self):
		return '{}.{}@gmail.com'.format(self.fname, self.lname)


	@fullname.setter
	def fullname(self,name):
		fname, lname = name.split(' ')

		self.fname = fname
		self.lname = lname

	@fullname.deleter
	def fullname(self):
		print("Delete Name")
		self.fname = None
		self.lname = None


e1 = Employee('Sayaji','Chavan',120000)
e2 = Employee('Nilesh','Bhise',120000)

e1.fullname = "Radha Krishna"
print(e2.fname)
print(e1.fname)
print("---------------------------------")

print(e1.email)
print(e1.fullname)
del e1.fullname

print(e1.fullname)