import unittest
from order import Order
from customer import Customer
from coffee import Coffee

class TestOrder(unittest.TestCase):
    def test_valid_order(self):
        customer = Customer("Leo")
        coffee = Coffee("Cappuccino")
        order = Order(customer, coffee, 4.0)

        self.assertEqual(order.customer, customer)
        self.assertEqual(order.coffee, coffee)
        self.assertEqual(order.price, 4.0)

    def test_invalid_price_type(self):
        customer = Customer("Leo")
        coffee = Coffee("Mocha")
        with self.assertRaises(TypeError):
            Order(customer, coffee, "cheap")

    def test_invalid_price_range(self):
        customer = Customer("Maya")
        coffee = Coffee("Flat White")

        with self.assertRaises(ValueError):
            Order(customer, coffee, 0.5)

        with self.assertRaises(ValueError):
            Order(customer, coffee, 11.0)

if __name__ == '__main__':
    unittest.main()
