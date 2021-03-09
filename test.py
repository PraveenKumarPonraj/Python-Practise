import unittest

from exercise import product_name_price


class ExerciseTestCase(unittest.TestCase):


    def test_nameandprice(self):

        result=product_name_price("fortune","one")

        self.assertEqual(result,"fortune one")