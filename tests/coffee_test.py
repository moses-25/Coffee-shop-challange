import unittest
from coffee import Coffee
from customer import Customer
from order import Order

class TestCoffee(unittest.TestCase):
    def test_valid_name(self):
        coffee = Coffee("Latte")
        self.assertEqual(coffee.name, "Latte")

    def test_invalid_name(self):
        with self.assertRaises(ValueError):
            Coffee("ab")

        with self.assertRaises(TypeError):
            Coffee(123)

    def test_immutable_name(self):
        coffee = Coffee("Latte")
        with self.assertRaises(AttributeError):
            coffee.name = "Mocha"

    def test_minimum_price(self):
    customer = Customer("Leo")
    coffee = Coffee("Americano")
    order = Order(customer, coffee, 1.0)
    self.assertEqual(order.price, 1.0)

    def test_no_orders(self):
    coffee = Coffee("Macchiato")
    self.assertEqual(coffee.num_orders(), 0)
    self.assertEqual(coffee.average_price(), 0)

    def test_orders_and_customers(self):
        coffee = Coffee("Espresso")
        c1 = Customer("Tom")
        c2 = Customer("Jane")

        c1.create_order(coffee, 3.0)
        c2.create_order(coffee, 4.0)

        self.assertEqual(coffee.num_orders(), 2)
        self.assertAlmostEqual(coffee.average_price(), 3.5)
        self.assertSetEqual(set(coffee.customers()), {c1, c2})

if __name__ == '__main__':
    unittest.main()
