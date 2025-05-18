from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from customer import Customer
    from coffee import Coffee

class Order:
    all = []

    def __init__(self, customer: customer, coffee: coffee, price: float):

        if customer.__class__.__name__ != "Customer":
            raise TypeError("Customer must be an instance of Customer.")
        if coffee.__class__.__name__ != "Coffee":
            raise TypeError("Coffee must be an instance of Coffee.")
        if not isinstance(price, float) or not (1.0 <= price <= 10.0):
            raise ValueError("Price must be a float between 1.0 and 10.0.")

        self._customer = customer
        self._coffee = coffee
        self._price = price
        Order.all.append(self)

    @property
    def customer(self) -> Customer:
        return self._customer

    @property
    def coffee(self) -> Coffee:
        return self._coffee

    @property
    def price(self) -> float:
        return self._price
