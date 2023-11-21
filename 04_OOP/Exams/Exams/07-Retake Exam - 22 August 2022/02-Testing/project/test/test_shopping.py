from unittest import TestCase, main
from project.shopping_cart import ShoppingCart


class Test(TestCase):
    def setUp(self) -> None:
        self.cart = ShoppingCart("Asd", 100.00)

    def test_correct_initialization(self):
        self.assertEqual("Asd", self.cart.shop_name)
        self.assertEqual(100.00, self.cart.budget)
        self.assertEqual({}, self.cart.products)

    def test_name_setter(self):
        expected = "Shop must contain only letters and must start with capital letter!"
        with self.assertRaises(ValueError) as ve:
            self.cart.shop_name = "asd"

        self.assertEqual(expected, str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.cart.shop_name = "A1sd"

        self.assertEqual(expected, str(ve.exception))

    def test_add_to_cart_if_expensive(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.add_to_cart('a', 100.01)

        self.assertEqual("Product a cost too much!", str(ve.exception))

    def test_add_to_card(self):
        res = self.cart.add_to_cart('a', 99)
        expected = "a product was successfully added to the cart!"

        self.assertEqual(expected, res)
        self.assertEqual({'a': 99}, self.cart.products)

    def test_remove_from_cart_if_not_exists(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.remove_from_cart('a')

        self.assertEqual("No product with name a in the cart!", str(ve.exception))

    def test_remove_from_cart(self):
        self.cart.products = {'a': 99, 'b': 12}
        res = self.cart.remove_from_cart('a')
        expected = "Product a was successfully removed from the cart!"

        self.assertEqual({'b': 12}, self.cart.products)
        self.assertEqual(expected, res)

    def test_add(self):
        other = ShoppingCart("Asd", 100.00)
        other.products = {'z': 10}
        self.cart.products = {'a': 10}
        # new = ShoppingCart("AsdAsd", 200.00)
        # new.products = {'a': 100, 'z': 100}

        res = self.cart.__add__(other)
        self.assertEqual("AsdAsd", res.shop_name)
        self.assertEqual(200.00, res.budget)
        self.assertEqual({'a': 10, 'z': 10}, res.products)

    def test_buy_product_if_not_enough_budget(self):
        self.cart.products = {'a': 55, 'z': 55}

        with self.assertRaises(ValueError) as ve:
            self.cart.buy_products()

        expected = "Not enough money to buy the products! Over budget with 10.00lv!"
        self.assertEqual(expected, str(ve.exception))

    def test_buy_product(self):
        self.cart.products = {'a': 15, 'z': 15}
        expected = "Products were successfully bought! Total cost: 30.00lv."

        self.assertEqual(expected, self.cart.buy_products())


if __name__ == "__main__":
    main()
