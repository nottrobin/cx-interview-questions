import unittest
from basket import Basket
from catalog import products


class TestBasket(unittest.TestCase):
    """
    Check the Basket performs as expected
    """

    def setUp(self):
        self.basket = Basket(product_catalog=products)
