class Employee():

	raise_amout = 10
	num_of_emps= 0
	def __init__(self, fname,lname,salary): #constructor 
		self.fname = fname
		self.lname = lname
		self.salary = salary
		self.email = fname + "." + lname + "@email.com"
		Employee.num_of_emps+= 1

	def fullname(self):
		return '{} {}'.format(self.fname, self.lname)

	def displaydata(self):
		return '{} {} {} {}'.format(self.fname, self.lname, self.salary, self.email)

	def applyraise(self):
		self.salary = int(self.salary * self.raise_amout)


	def __add__(self,other):
		return self.salary + other.salary


	def __repr__(self):
		return '{} - {} - {}'.format(self.fname, self.lname, self.salary)

	def __str__(self):
		return '{} {} {}'.format(self.fname, self.lname, self.salary)

	def __len__(self):
		return len(self.fname)

 



class Developer(Employee): #class Developer inheriting from Employee Class
	raise_amout = 1.5   #by changing the amount here the instance will use this raise amount instead of Parent classes raise amount.
	def __init__(self,fname,lname,salary,stack):
		super().__init__(fname,lname,salary)
		self.stack = stack


class manager(Employee):
	def __init__(self,fname,lname,salary,employees = None):
		super().__init__(fname,lname,salary)
		if employees is None:
			self.employees = []
		else:
			self.employees = employees

	def add_emp(self,emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emp(self,emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def print_emp(self):
		for emp in self.employees:
			print('-->',emp.fullname())

		


dev1 = Employee("Sayaji","Chavan",400000)
dev2 = Employee("Nilesh","Bhise",400000)



print(dev1.__str__())
print(dev1.__repr__())
print()
print(dev1 + dev2)
print(len(dev1))