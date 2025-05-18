import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer(unittest.TestCase):
    def test_valid_name(self):
        c = Customer("Sam")
        self.assertEqual(c.name, "Sam")

    def test_invalid_name_type(self):
        with self.assertRaises(TypeError):
            Customer(123)

    def test_invalid_name_length(self):
        with self.assertRaises(ValueError):
            Customer("")

        with self.assertRaises(ValueError):
            Customer("A" * 16)

    def test_set_name_valid(self):
        c = Customer("Sam")
        c.name = "Max"
        self.assertEqual(c.name, "Max")

    def test_minimum_price(self):
    customer = Customer("Leo")
    coffee = Coffee("Americano")
    order = Order(customer, coffee, 1.0)
    self.assertEqual(order.price, 1.0)

    def test_no_orders(self):
    coffee = Coffee("Macchiato")
    self.assertEqual(coffee.num_orders(), 0)
    self.assertEqual(coffee.average_price(), 0)

    def test_set_name_invalid(self):
        c = Customer("Sam")
        with self.assertRaises(ValueError):
            c.name = "A" * 16

    def test_create_order_and_relationships(self):
        c = Customer("Anna")
        coffee = Coffee("Latte")
        order = c.create_order(coffee, 3.5)

        self.assertIn(order, c.orders())
        self.assertIn(coffee, c.coffees())

if __name__ == '__main__':
    unittest.main()
