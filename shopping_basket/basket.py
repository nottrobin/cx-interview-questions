class Basket():
    """
    A collection of products that a customer intends to purchase,
    with methods allowing you to calculate the subtotal and total
    price of all products, potentially with offers applied.
    """

    products = []

    def __init__(self, product_catalog):
        self.product_catalog = product_catalog

    def add_product(self, sku):
        self.products.append(sku)
