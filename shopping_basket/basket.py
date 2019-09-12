class Basket():
    """
    A collection of products that a customer intends to purchase,
    with methods allowing you to calculate the subtotal and total
    price of all products, potentially with offers applied.
    """

    def __init__(self, product_catalog):
        self.product_catalog = product_catalog
