def summarize_orders(orders: list[dict[str, object]]) -> dict[str, object]:
    count = 0
    total = 0.0
    by_customer: dict[str, float] = {}

    for order in orders:
        customer = order.get("customer")
        amount = order.get("amount")
        if not isinstance(customer, str) or not isinstance(amount, int | float):
            continue

        count += 1
        total += float(amount)
        by_customer[customer] = by_customer.get(customer, 0.0) + float(amount)

    return {"count": count, "total": total, "by_customer": by_customer}
