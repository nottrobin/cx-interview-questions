class Basket():
    """
    A collection of products that a customer intends to purchase,
    with methods allowing you to calculate the subtotal and total
    price of all products, potentially with offers applied.
    """

    def __init__(self, product_catalog):
        self.product_catalog = product_catalog
        self.products = []

    def add_product(self, sku):
        """
        Add a product sku to the basket.

        We're not adding any more information at this stage, as we should
        only look up the product in the catalog at the last minute so we
        get the most up-to-date price for each item.
        """

        self.products.append(sku)

    def subtotal(self):
        """
        Calculate the subtotal of all products in the basket
        """

        subtotal = 0

        for sku in self.products:
            subtotal += self.product_catalog[sku]["price"]

        return round(subtotal, 2)
