# Standard library
import math
from typing import Dict, List

# Local modules
from offers import Offer


def _round_price(number: float):
    """
    Round to the nearest 2 decimal places, rounding half up.
    This avoids the issue with Python's native `round` function
    using a "round to even" strategy.

    From https://realpython.com/python-rounding/#rounding-half-up
    """

    return math.floor(number * 100 + 0.5) / 100


class Basket:
    """
    A collection of products that a customer intends to purchase,
    with methods allowing you to calculate the subtotal and total
    price of all products, potentially with offers applied.
    """

    def __init__(
        self, product_catalog: Dict[str, Dict], offers: List[Offer] = []
    ):
        self.product_catalog = product_catalog
        self.product_skus = []
        self.offers = offers

    def add_product(self, sku) -> None:
        """
        Add a product sku to the basket.

        We're not adding any more information at this stage, as we should
        only look up the product in the catalog at the last minute so we
        get the most up-to-date price for each item.
        """

        self.product_skus.append(sku)

    def subtotal(self) -> float:
        """
        Calculate the subtotal of all products in the basket
        """

        subtotal = 0

        for sku in self.product_skus:
            subtotal += self.product_catalog[sku]["price"]

        return _round_price(subtotal)

    def discount(self) -> float:
        """
        Given the set of products in the basket and the available offers,
        calculate the total discount
        """

        total_discount = 0
        products = [self.product_catalog[sku] for sku in self.product_skus]

        for offer in self.offers:
            total_discount += offer.calculate_discount(products=products)

        return _round_price(total_discount)

    def total(self) -> float:
        """
        Calculate the total from the subtotal and the discount
        """

        return self.subtotal() - self.discount()
