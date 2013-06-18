import unittest
from ex1_circle import circleArea

class testCircle(unittest.TestCase):
	
	def test_area_1st(self):
		self.assertEqual(int(circleArea(3)),28)
	
	def test_area_2nd(self):
		self.assertEqual(int(circleArea(3.0)),28)
	
	def test_area_3rd(self):
		self.assertEqual(int(circleArea("3.0")),28)
	
if __name__ == '__main__':
	unittest.main()