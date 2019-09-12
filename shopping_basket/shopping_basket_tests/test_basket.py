# Standard library
import unittest

# Local modules
import catalog
from basket import Basket
from offers import GetOneFree, PercentageDiscount


class TestBasket(unittest.TestCase):
    """
    Check the Basket performs as expected
    """

    def setUp(self):
        """
        Create the two baskets described in assignment.py
        """

        offers = [
            GetOneFree(
                product_sku="beans",
                min_items=2,
                product_catalog=catalog.products,
            ),
            PercentageDiscount(
                product_sku="sardines",
                discount_percent=25,
                product_catalog=catalog.products,
            )
        ]

        self.basket_1 = Basket(product_catalog=catalog.products, offers=offers)

        self.basket_1.add_product("beans")
        self.basket_1.add_product("beans")
        self.basket_1.add_product("beans")
        self.basket_1.add_product("beans")
        self.basket_1.add_product("biscuits")

        self.basket_2 = Basket(product_catalog=catalog.products, offers=offers)

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

    def test_discount(self):
        """
        Check discount() tells us how much is discounted based on added offers
        """

        self.assertEqual(self.basket_1.discount(), 0.99)
        self.assertEqual(self.basket_2.discount(), 0.95)

    def test_total(self):
        """
        Check total() returns the expected total for both baskets
        """

        self.assertEqual(self.basket_1.total(), 4.17)
        self.assertEqual(self.basket_2.total(), 6.01)
