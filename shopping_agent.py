# My First Agentic Commerce Project

products = {
    "Laptop": 899,
    "Headphones": 149,
    "Smartwatch": 249
}

budget = 300

print("Welcome to Agentic Commerce Lab!")
print(f"Your shopping budget: ${budget}")

print("\nProducts within your budget:")

for product, price in products.items():
    if price <= budget:
        print(f"{product}: ${price}")
