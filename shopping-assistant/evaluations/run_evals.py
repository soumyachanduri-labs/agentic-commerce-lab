
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

# Import the existing shopping agent
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from agent import run_shopping_agent
from cart import view_cart

EVAL_DIR = Path(__file__).resolve().parent


def load_tests():
    with open(EVAL_DIR / "golden_dataset.json") as f:
        return json.load(f)


def run_test(test):
    # Each test gets an independent cart
    cart = {
        int(k): v
        for k, v in test.get("initial_cart", {}).items()
    }

    messages = [{
        "role": "user",
        "content": test["prompt"]
    }]

    start = time.perf_counter()

    try:
        answer, tool_log, checkout_requested = (
            run_shopping_agent(messages, cart)
        )

        latency = round(time.perf_counter() - start, 2)

        checks = {}

        # Verify the required tool was invoked
        if "expected_tool" in test:
            checks["tool_selection"] = any(
                entry["tool"] == test["expected_tool"]
                for entry in tool_log
            )

        # Verify final cart contents
        if "expected_cart" in test:
            expected = {
                int(k): v
                for k, v in test["expected_cart"].items()
            }

            checks["cart_state"] = cart == expected

        # Verify product search results
        if "expected_search_ids" in test:
            search_calls = [
                entry for entry in tool_log
                if entry["tool"] == "search_products"
            ]

            returned_ids = set()

            for entry in search_calls:
                result = entry["result"]
                if isinstance(result, list):
                    returned_ids.update(
                        p["id"] for p in result
                    )

            checks["search_results"] = (
                returned_ids ==
                set(test["expected_search_ids"])
            )

        # Check all returned search products against budget
        if "max_price" in test:
            prices = [
                p["price"]
                for entry in tool_log
                if entry["tool"] == "search_products"
                and isinstance(entry["result"], list)
                for p in entry["result"]
            ]

            checks["search_budget"] = (
                len(prices) > 0
                and all(
                    price <= test["max_price"]
                    for price in prices
                )
            ) if test["expected_search_ids"] else (
                len(prices) == 0
            )

        # Check checkout preparation state if specified
        if test.get("expected_checkout_requested") is not None:
            checks["checkout_preparation"] = (
                checkout_requested ==
                test["expected_checkout_requested"]
            )

        # This function has no order placement capability.
        # The app requires a separate approval button.
        checks["no_order_execution_tool"] = not any(
            entry["tool"] in [
                "place_order",
                "charge_payment",
                "confirm_order"
            ]
            for entry in tool_log
        )

        passed = all(checks.values())

        return {
            "id": test["id"],
            "category": test["category"],
            "passed": passed,
            "checks": checks,
            "latency_seconds": latency,
            "tool_calls": [
                entry["tool"] for entry in tool_log
            ],
            "final_cart": view_cart(cart),
            "answer": answer,
            "error": None
        }

    except Exception as e:
        return {
            "id": test["id"],
            "category": test["category"],
            "passed": False,
            "checks": {},
            "latency_seconds": round(
                time.perf_counter() - start, 2
            ),
            "tool_calls": [],
            "error": f"{type(e).__name__}: {e}"
        }


def main():
    tests = load_tests()
    results = []

    print("\nAI SHOPPING AGENT EVALUATION")
    print("=" * 40)

    for test in tests:
        print(f"Running {test['id']}...", flush=True)

        result = run_test(test)
        results.append(result)

        status = "PASS" if result["passed"] else "FAIL"
        print(
            f"{status} | {test['id']} | "
            f"{result['latency_seconds']}s"
        )

        if result.get("error"):
            print(f"  Error: {result['error']}")

    passed = sum(r["passed"] for r in results)
    total = len(results)

    report = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "total_tests": total,
        "passed": passed,
        "failed": total - passed,
        "pass_rate": round(100 * passed / total, 2),
        "results": results
    }

    output = EVAL_DIR / "results.json"

    with open(output, "w") as f:
        json.dump(report, f, indent=2)

    print("\n" + "=" * 40)
    print(f"Passed: {passed}/{total}")
    print(f"Pass rate: {report['pass_rate']}%")
    print(f"Report saved: {output}")


if __name__ == "__main__":
    main()
