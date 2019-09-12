# Standard library
from typing import List, Dict


def _chunks(list_to_split, size):
    """
    Yield successive n-sized chunks from list_to_split.
    From https://stackoverflow.com/a/312464/613540
    """

    for index in range(0, len(list_to_split), size):
        end = index + size
        yield list_to_split[index:end]


class Offer:
    """
    An interface class that defines the "calculate_discount" method
    """

    def calculate_discount(products: List[Dict]):
        raise NotImplementedError()


class GetOneFree(Offer):
    """
    An offer where you get one item free if you buy x items
    """

    def __init__(
        self,
        product_sku: str,
        min_items: int,
        product_catalog: Dict[str, Dict],
    ):
        self.product_sku = product_sku
        self.min_items = min_items
        self.product_catalog = product_catalog

    def calculate_discount(self, skus: List[str]) -> float:
        """
        Given a list of products, check if this discount applies
        to any of them, and apply the discount if it does
        """

        valid_items = [sku for sku in skus if sku == self.product_sku]
        discount = 0

        for chunk in _chunks(valid_items, self.min_items + 1):
            if len(chunk) == self.min_items + 1:
                discount += self.product_catalog[self.product_sku]["price"]

        return discount
