import unittest
import Parser

file_dict = {}

object = Parser.Parser(file_dict)

class TestParser(unittest.TestCase):

	def test_float(self):
		self.assertTrue(object.check_float("70.0"))


if __name__ == '__main__':
	unittest.main() 


	
	 