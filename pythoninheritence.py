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

		


dev1 = Developer("Sayaji","Chavan",400000,'java')
dev2 = Developer("Nilesh","Bhise",400000,'python')


mgr = manager("Laxman","Chavan",251351,[dev1])
 
print(isinstance(mgr,manager)) # to check if mgr is an instance of Manager class

print(isinstance(mgr,Developer)) #
 

print(issubclass(Developer, Employee)) #to check if Developer is subclass of Employee

print(issubclass(manager,Employee)) #to check is manager is subclass of EMployee

print(str(dev1))