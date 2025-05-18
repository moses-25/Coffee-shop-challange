from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from customer import Customer
    from coffee import Coffee

class Coffee:
    def __setattr__(self, name, value):
        if name == "_name" and hasattr(self, "_name"):
            raise AttributeError("Cannot modify the name of a Coffee.")
        super().__setattr__(name, value)
        
    def __init__(self, name,):
        if isinstance(name, str) and len(name) >= 3:
            self._name = name
        else:
            raise ValueError("Name must be a string with at least 3 characters.")

    @property
    def name(self):
        return self._name

    def orders(self):
        return [order for order in Order.all if order.coffee == self]

    def customers(self):
        return list({order.customer for order in self.orders()})

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        prices = [order.price for order in self.orders()]
        return sum(prices) / len(prices) if prices else 0
