class time():
	def __init__(self, hours, minutes, seconds):
		self.hours = hours
		self.minutes = minutes
		self.seconds = seconds

	def displaytime(self):
		return ' The time is {} hours, {} minutes and {} seconds'.format(self.hours, self.minutes, self.seconds)

	@classmethod #decorator the below method is a class method
	def from_string(cls,strstime): #the first parameter to pass in class method is cls and then 2nds parameter
		hours, minutes, seconds = strstime.split(',')
		return cls(hours, minutes,seconds) #returning into to class
		#can also be written as time(hours, minutes and seconds) 

	@staticmethod
	def is_workday(day):
		if day.weekday == 5 or day.weekday == 6:
			return False
		return True


str1 = "15,26,45"

import datetime

my_date = datetime.date(2021,10,10)
print(time.is_workday(my_date))



#newtime = time.from_string(str1) #creating an instance of the class and passing the string to the from_string function of the class 
#print(time.displaytime(newtime))
	
