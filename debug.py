from customer import Customer
from coffee import Coffee
from order import Order

# --- Create Customers ---
alice = Customer("Alice")
bob = Customer("Bob")

# --- Create Coffees ---
latte = Coffee("Latte")
espresso = Coffee("Espresso")

# --- Create Orders ---
order1 = alice.create_order(latte, 3.5)
order2 = alice.create_order(espresso, 4.0)
order3 = bob.create_order(latte, 5.0)

# --- Check Relationships ---
print("\n--- Customer Orders ---")
print([o.price for o in alice.orders()])  # Should show [3.5, 4.0]
print([c.name for c in alice.coffees()])  # Should show ['Latte', 'Espresso']

print("\n--- Coffee Orders ---")
print([o.price for o in latte.orders()])  # Should show [3.5, 5.0]
print([c.name for c in latte.customers()])  # Should show ['Alice', 'Bob']

print("\n--- Coffee Aggregates ---")
print(latte.num_orders())  # Should show 2
print(latte.average_price())  # Should show 4.25

print("\n--- Aficionado Check ---")
aficionado = Customer.most_aficionado(latte)
print(aficionado.name if aficionado else "No aficionado")  # Should show Bob

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
    bad_order = Order(alice, latte, 20.0)  # Invalid price
except ValueError as e:
    print(e)
    
