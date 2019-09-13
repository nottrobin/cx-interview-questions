# Shopping basket

[![CircleCI build status](https://circleci.com/gh/nottrobin/cx-interview-questions.svg?style=shield)](https://circleci.com/gh/nottrobin/cx-interview-questions "CircleCI build status")
[![Code coverage](https://codecov.io/gh/nottrobin/cx-interview-questions/branch/master/graph/badge.svg)](https://codecov.io/gh/nottrobin/cx-interview-questions "Code coverage")

A shopping basket object for calculating the summary, discount and total price of a collection of products.

This is my solution to [the shopping-basket assignment](https://github.com/ecs-cx/cx-interview-questions/blob/master/shopping_basket/assignment.md).

## Usage

This implementation requires Python 3.6 or greater.

The `Basket` class is contained in [`basket.py`](basket.py#L21). It makes use of the products defined in [`catalog.py`](catalog.py) and the offer classes in [`offers.py`](offers.py).

You can use the `Basket` class to add and make calculations on products as illustrated below:

``` python3
import catalog
from basket import Basket
from offers import CheapestFree, GetOneFree, PercentageDiscount

basket = Basket(
    product_catalog=catalog.products,
    offers=[
        GetOneFree(product_sku="beans", min_items=2),
        PercentageDiscount(product_sku="sardines", discount_percent=25),
        CheapestFree(product_category="shampoo", min_items=3)
    ]
)

basket.add_product("beans")
basket.add_product("biscuits")
basket.add_product("sardines")
basket.add_product("shampoo-m")

print("Subtotal: £" + basket.subtotal())
print("Discount: £" + basket.discount())
print("Total: £" + basket.total())
```

## Running tests

The test scenarios in the assignment have been used in [the tests](shopping_basket_tests/test_basket.py).

The tests can be run as follows, from within the `shopping_basket` directory of this repository:

``` bash
python3 -m unittest discover shopping_basket_tests
```
