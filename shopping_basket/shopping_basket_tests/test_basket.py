import unittest
import catalog
from basket import Basket


class TestBasket(unittest.TestCase):
    """
    Check the Basket performs as expected
    """

    def setUp(self):
        """
        Create the two baskets described in assignment.py
        """

        self.basket_1 = Basket(product_catalog=catalog.products)

        self.basket_1.add_product("beans")
        self.basket_1.add_product("beans")
        self.basket_1.add_product("beans")
        self.basket_1.add_product("beans")
        self.basket_1.add_product("biscuits")

        self.basket_2 = Basket(product_catalog=catalog.products)

        self.basket_2.add_product("beans")
        self.basket_2.add_product("beans")
        self.basket_2.add_product("biscuits")
        self.basket_2.add_product("sardines")
        self.basket_2.add_product("sardines")

    def test_subtotal(self):
        """
        Check subtotal() returns the expected sum of all products' prices
        """

        self.assertEqual(self.basket_1.subtotal(), 5.16)
        self.assertEqual(self.basket_2.subtotal(), 6.96)
