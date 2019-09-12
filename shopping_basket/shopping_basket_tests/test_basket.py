import unittest
from basket import Basket


class TestBasket(unittest.TestCase):
    """
    Check the Basket performs as expected
    """

    def setUp(self):
        self.basket = Basket()
