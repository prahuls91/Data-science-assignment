class Employee:
	empCount= 0

	def __init__(self,name,age):
		self.name=name
		self.age=age
		Employee.empCount +=1


	def displayCount(self):
		print("total Employee %d" % Employee.empCount)

	def displayEmployee(self):	
		print("Name:",self.name,"age:",self.age)
Emp1=Employee("x",26)
Emp2=Employee("y",28)
Emp1.displayEmployee()
Emp2.displayEmployee()
print("total Employee %d" % Employee.empCount)