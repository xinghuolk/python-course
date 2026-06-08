def calculate_total(
    prices: list[float],
    tax_rate: float = 0.0,
    discount: float = 0.0,
) -> float:
    subtotal = sum(prices)
    discounted = subtotal * (1 - discount)
    taxed = discounted * (1 + tax_rate)
    return round(taxed, 2)
