import unittest
from unit import SuperMarket


class TestUnit(unittest.TestCase):

    def test_nameandprice(self):
        product_1 = SuperMarket('rice','one')
        product_2 = SuperMarket('wheet','two')


        self.assertEqual(product_1.nameandprice,'rice-one')
        self.assertEqual(product_2.nameandprice,'wheet-two')

     

if __name__ == '__main__':
    unittest.main()   