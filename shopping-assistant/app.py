
import json
from pathlib import Path
import streamlit as st

# Load products from our local catalog
catalog_path = Path(__file__).parent / "products.json"

with open(catalog_path, "r", encoding="utf-8") as file:
    products = json.load(file)

# Page configuration
st.set_page_config(
    page_title="Agentic Shopping Assistant",
    page_icon="🛍️",
    layout="wide"
)

st.title("🛍️ Agentic Shopping Assistant")
st.write("Discover products that match your needs.")

# User-controlled filters
category = st.selectbox(
    "Choose a category",
    ["All", "Headphones", "Smartwatches"]
)

max_price = st.slider(
    "Maximum price ($)",
    min_value=0,
    max_value=300,
    value=150
)

# Filter the catalog
filtered_products = []

for product in products:
    category_matches = (
        category == "All"
        or product["category"] == category
    )

    price_matches = product["price"] <= max_price

    if category_matches and price_matches:
        filtered_products.append(product)

# Display matching products
st.subheader("Recommended Products")

if not filtered_products:
    st.warning("No products match your filters.")

for product in filtered_products:
    with st.container(border=True):
        st.subheader(product["name"])
        st.write(f"Price: ${product['price']:.2f}")
        st.write(f"Rating: {product['rating']} / 5")
        st.write(
            "Features: " + ", ".join(product["features"])
        )
