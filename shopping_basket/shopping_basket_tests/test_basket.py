#! /usr/bin/env python3

# Standard library
import unittest

# Local modules
import catalog
from basket import Basket
from offers import CheapestFree, GetOneFree, PercentageDiscount


class TestBasket(unittest.TestCase):
    """
    Check the Basket performs as expected
    """

    def setUp(self):
        """
        Create the two baskets described in assignment.py
        """

        offers = [
            GetOneFree(product_sku="beans", min_items=2),
            PercentageDiscount(product_sku="sardines", discount_percent=25),
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

    def test_basket_3(self):
        """
        Check subtotal, discount and total are as expected for basket 3
        """

        basket_3 = Basket(
            product_catalog=catalog.products,
            offers=[CheapestFree(product_category="shampoo", min_items=3)],
        )

        basket_3.add_product("shampoo-l")
        basket_3.add_product("shampoo-l")
        basket_3.add_product("shampoo-l")
        basket_3.add_product("shampoo-m")
        basket_3.add_product("shampoo-s")
        basket_3.add_product("shampoo-s")

        self.assertEqual(basket_3.subtotal(), 17)
        self.assertEqual(basket_3.discount(), 5.5)
        self.assertEqual(basket_3.total(), 11.5)


if __name__ == "__main__":
    unittest.main()
