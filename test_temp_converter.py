import unittest
from temp_converter import convert_celcius_tofarenheight

class Tempconverter(unittest.TestCase):
	# Given the temp in celcius = correct value in F
	# null values => throw an error, return false, return some string
	# data type for input
	# if throws error
	def test_celcius_is_converted_to_fareinheights(self):
		"""

		F = c * 9/5 + 32

		"""
		actual = convert_celcius_tofarenheight(10)
		expected = 50
		self.assertEqual(actual, expected, 'Celcius should convert to correct farenheights')
		self.assertEqual(convert_celcius_tofarenheight(20), 68, 'Celcius should convert to correct farenheights')