import unittest


class ProductList:
    def __init__(self) -> None:
        self.operands = []

    def add(self, n: int) -> None:
        self.operands.append(n)

    def product(self, n: int) -> int:
        if len(self.operands) < n:
            raise Exception("ProductList is not long enough")
        prod = 1
        for i in range(1, n + 1):
            prod *= self.operands[-i]
        return prod


class TestProductList(unittest.TestCase):
    def test_example(self):
        p = ProductList()
        p.add(7)
        p.add(0)
        p.add(2)
        p.add(5)
        p.add(4)
        self.assertEqual(p.product(3), 40)

    def test_raises_exception(self):
        p = ProductList()
        self.assertRaises(
            Exception, lambda: p.product(1), msg="ProductList is not long enough"
        )

    def test_multiplies_products_with_zero(self):
        p = ProductList()
        p.add(0)
        p.add(10)
        self.assertEqual(p.product(2), 0)

    def test_handles_list_of_length_one(self):
        p = ProductList()
        p.add(7)
        self.assertEqual(p.product(1), 7)

    def test_returns_one_for_negative_product_argument(self):
        p = ProductList()
        self.assertEqual(p.product(-1), 1)

    def test_returns_one_for_zero_product_argument(self):
        p = ProductList()
        self.assertEqual(p.product(0), 1)