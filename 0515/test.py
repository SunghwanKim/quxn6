class TestClass :
	def __init__(self, name)	:
		self.name = name

	def getName(self)	:
		return self.name

	def setName(self, name)	:
		self.name = name

from test import TestClass
obj = TestClass("KIA")
obj.getName()

