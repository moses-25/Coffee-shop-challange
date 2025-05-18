# Coffee-shop-challange

A Python-based project that models a coffee shop system, including customers, coffee types, and orders. This project demonstrates object-oriented programming concepts, relationships between entities, and basic error handling.

## Overview

The Coffee Shop Challenge is a simulation of a coffee shop system where:
- Customers can place orders for different types of coffee.
- Orders track the customer, coffee type, and price.
- Coffees track their orders and calculate statistics like the number of orders and average price.

This project is designed to showcase object-oriented programming principles such as encapsulation, relationships, and immutability.

---

## Features

- **Customer Management**: Create customers with valid names and track their orders.
- **Coffee Management**: Define coffee types with immutable names and track orders associated with each coffee.
- **Order Management**: Create orders with valid prices and establish relationships between customers and coffees.
- **Statistics**:
  - Number of orders for a coffee.
  - Average price of orders for a coffee.
  - Identify the most loyal customer (aficionado) for a coffee.
- **Error Handling**: Validate inputs and raise appropriate exceptions for invalid data.

---

## Project Structure
coffee-shop-challenge/
  ├── Pipfile # Dependency management
  ├── debug.py # Demo script
  ├── customer.py # Customer class
  ├── coffee.py # Coffee class
  ├── order.py # Order class
└── tests/
        ├── init.py
        ├── customer_test.py # Customer unit tests
        ├── coffee_test.py # Coffee unit tests
        └── order_test.py # Order unit tests