class Vehicle:
	def __init__(self,name,color):
		self.name=name
		self.color=color
	def getColor(self):
		return self.color

	def setColor(self,color):
		self.color=color

	def getName(self):
		self.name

class Car(Vehicle):

	def __init__(self,name,color,model):
		super().__init__(name,color)
		self.model=model

	def getDescription(self):
		return self.getName()+self.model+self.color()+color

c=Car("Lexus","Grey","SUV")
print(c.getDescription())
print(c.getName())