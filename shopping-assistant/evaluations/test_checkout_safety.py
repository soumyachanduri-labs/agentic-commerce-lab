
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from cart import (
    add_to_cart,
    prepare_checkout,
    view_cart
)


def test_checkout_requires_separate_approval():
    cart = {}

    add_to_cart(cart, product_id=3, quantity=1)

    checkout = prepare_checkout(cart)

    assert checkout["status"] == "awaiting_approval"
    assert checkout["order_summary"]["subtotal"] == "149.99"

    # Preparing checkout must not clear the cart
    assert cart == {3: 1}


def test_invalid_product_rejected():
    cart = {}

    result = add_to_cart(cart, product_id=999)

    assert "error" in result
    assert view_cart(cart)["items"] == []


def test_invalid_quantity_rejected():
    cart = {}

    result = add_to_cart(
        cart,
        product_id=3,
        quantity=100
    )

    assert "error" in result
    assert cart == {}
