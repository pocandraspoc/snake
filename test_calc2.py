import unittest
import calc2

class TestCalc2(unittest.TestCase):

	def test_add(self):
		result = calc2.add(10,3)
		self.assertEqual(result, 13)
	
	def test_sub(self):
		result = calc2.sub(6,1)
		self.assertEqual(result, 5)

	def test_multi(self):
		result = calc2.multi(3,4)
		res2 = calc2.multi(70, 2)
		self.assertEqual(result, 12)
		self.assertEqual(res2, 140)

	def test_dev(self):
		result = calc2.devide(10,5)
		res2 = calc2.devide(300,60)
		self.assertEqual(result, 2)
		self.assertEqual(res2, 5)

if __name__ == '__main__':
	unittest.main()