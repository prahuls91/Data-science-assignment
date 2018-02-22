class arithmetic_operations:
	def__init__(self):
	print("constructor got called")

	def add(self,a,b):
		return a+b
	def sub(self,a,b):
		return a-b
	def divide(self,a,b):
		return a/b
	def mult(self,a,b):
		return a*b

Obj1=arithmetic_operations()
Obj1.add(20,10)
Obj1.sub(20,10)
Obj1.divide(20,10)
Obj1.mult(20/10)