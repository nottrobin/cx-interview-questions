import unittest
from basket import Basket
from catalog import products


class TestBasket(unittest.TestCase):
    """
    Check the Basket performs as expected
    """

    def setUp(self):
        self.basket = Basket(product_catalog=products)

    def test_add_product(self):
        self.basket.add_product("beans")
        self.basket.add_product("shampoo-l")
        self.assertEqual(len(self.basket.products), 2)
