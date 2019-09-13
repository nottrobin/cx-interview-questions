# Standard library
from typing import List, Dict


def _chunks(list_to_split, size):
    """
    Yield successive chunks of the specified size from list_to_split.
    From https://stackoverflow.com/a/312464/613540
    """

    for index in range(0, len(list_to_split), size):
        end = index + size
        yield list_to_split[index:end]


class Offer:
    """
    An interface class that defines the "calculate_discount" method
    """

    def calculate_discount(self, products: List[Dict]):
        """
        Given a list of products, check if this discount applies
        to any of them, and apply the discount if it does
        """

        raise NotImplementedError()  # pragma: no cover


class GetOneFree(Offer):
    """
    An offer where you get one item free if you buy x items
    """

    def __init__(self, product_sku: str, min_items: int) -> None:
        self.product_sku = product_sku
        self.min_items = min_items

    def calculate_discount(self, products: List[Dict]) -> float:
        """
        Given a list of products, check if this discount applies
        to any of them, and apply the discount if it does
        """

        discount = 0.0
        valid_products = []

        for product in products:
            if product["sku"] == self.product_sku:
                valid_products.append(product)

        for chunk in _chunks(valid_products, self.min_items + 1):
            if len(chunk) == self.min_items + 1:
                discount += valid_products[0]["price"]

        return discount


class CheapestFree(Offer):
    """
    An offer where you get the cheapest item free from items in a specific
    category
    """

    def __init__(self, product_category: str, min_items: int) -> None:
        self.product_category = product_category
        self.min_items = min_items

    def calculate_discount(self, products: List[Dict]) -> float:
        """
        Given a list of products, check if this discount applies
        to any of them, and apply the discount if it does
        """

        discount = 0.0
        valid_items = []

        for product in products:
            if product.get("category") == self.product_category:
                valid_items.append(product)

        # Sort items by descending price so customers get the maximum discount
        valid_items.sort(key=lambda product: product["price"], reverse=True)

        for chunk in _chunks(valid_items, self.min_items):
            if len(chunk) == self.min_items:
                # The last item will be the cheapest
                discount += chunk[self.min_items - 1]["price"]

        return discount


class PercentageDiscount(Offer):
    """
    An offer where an item gets a percentage discount
    """

    def __init__(self, product_sku: str, discount_percent: float) -> None:
        self.product_sku = product_sku
        self.discount_percent = discount_percent

    def calculate_discount(self, products: List[Dict]) -> float:
        """
        Given a list of products, check if this discount applies
        to any of them, and apply the discount if it does
        """

        discount = 0.0
        valid_products = []

        for product in products:
            if product["sku"] == self.product_sku:
                valid_products.append(product)

        if valid_products:
            price = valid_products[0]["price"]
            discount_per_item = price * self.discount_percent / 100
            discount = discount_per_item * len(valid_products)

        return discount
