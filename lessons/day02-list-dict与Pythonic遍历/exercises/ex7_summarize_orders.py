def summarize_orders(orders: list[dict[str, object]]) -> dict[str, object]:
    """汇总订单列表。

    每个订单形如：{"customer": "alice", "amount": 12.5}

    返回：
    {
        "count": 订单总数,
        "total": 总金额,
        "by_customer": {"alice": 12.5, ...}
    }

    缺少 customer 或 amount 的订单忽略。
    """
    # TODO: 汇总 count、total、by_customer
    raise NotImplementedError
