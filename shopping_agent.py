# My First Agentic Commerce Project


# Agentic Commerce Lab
# Version 1: Basic Shopping Assistant

products = [
    {
        "name": "Wireless Pro Headphones",
        "category": "headphones",
        "price": 149,
        "rating": 4.7
    },
    {
        "name": "Studio Noise-Canceling Headphones",
        "category": "headphones",
        "price": 249,
        "rating": 4.9
    },
    {
        "name": "Everyday Bluetooth Headphones",
        "category": "headphones",
        "price": 79,
        "rating": 4.3
    },
    {
        "name": "Smartwatch Active",
        "category": "smartwatch",
        "price": 199,
        "rating": 4.5
    },
    {
        "name": "Smartwatch Ultra",
        "category": "smartwatch",
        "price": 399,
        "rating": 4.8
    },
    {
        "name": "Laptop Air 13",
        "category": "laptop",
        "price": 899,
        "rating": 4.6
    },
    {
        "name": "Laptop Student",
        "category": "laptop",
        "price": 599,
        "rating": 4.4
    }
]


def find_products(category, budget):
    matches = []

    for product in products:
        if (
            product["category"] == category
            and product["price"] <= budget
        ):
            matches.append(product)

    # Rank by customer rating, highest first
    matches.sort(
        key=lambda p: p["rating"],
        reverse=True
    )

    return matches


def main():
    print("Welcome to Agentic Commerce Lab!")

    print("\nAvailable categories:")
    print("headphones, smartwatch, laptop")

    category = input(
        "\nWhat are you shopping for? "
    ).strip().lower()

    try:
        budget = float(input(
            "What is your maximum budget ($)? "
        ))
    except ValueError:
        print("Please enter a valid budget.")
        return

    if budget < 0:
        print("Budget cannot be negative.")
        return

    recommendations = find_products(
        category, budget
    )

    print("\nRecommended products:")

    if not recommendations:
        print("No matching products found.")
        return

    for product in recommendations:
        print(
            f"{product['name']} | "
            f"${product['price']} | "
            f"Rating: {product['rating']}/5"
        )


if __name__ == "__main__":
    main()

