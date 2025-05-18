from customer import Customer
from coffee import Coffee
from order import Order

# this Create Customers 
moses = Customer("Moses")
joseph = Customer("Joseph")

# this Create Coffees 
latte = Coffee("Latte")
espresso = Coffee("Espresso")

# this Create Orders
order1 = moses.create_order(latte, 3.5)
order2 = moses.create_order(espresso, 4.0)
order3 = joseph.create_order(latte, 5.0)

# this Checks Relationships
print("\n--- Customer Orders ---")
print([o.price for o in moses.orders()])  
print([c.name for c in moses.coffees()])

print("\n--- Coffee Orders ---")
print([o.price for o in latte.orders()])  # Should show [3.5, 5.0]
print([c.name for c in latte.customers()])  # Should show ['moses', 'joseph']

print("\n--- Coffee Aggregates ---")
print(latte.num_orders())  # Should show 2
print(latte.average_price())  # Should show 4.25

print("\n--- Aficionado Check ---")
aficionado = Customer.most_aficionado(latte)
print(aficionado.name if aficionado else "No aficionado")  # Should show 'moses'

# --- Error Handling Examples ---
print("\n--- Error Handling ---")
try:
    bad_customer = Customer("ThisNameIsWayTooLong")
except ValueError as e:
    print(e)

try:
    bad_coffee = Coffee("Yo")
except ValueError as e:
    print(e)

try:
    bad_order = Order(moses, latte, 20.0)  # Invalid price
except ValueError as e:
    print(e)
