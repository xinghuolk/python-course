def calculate_total(
    prices: list[float],
    tax_rate: float = 0.0,
    discount: float = 0.0,
) -> float:
    """计算订单总价。

    规则：
    - subtotal = prices 的总和；
    - discount 是折扣比例，0.1 表示九折；
    - 先打折，再加税；
    - 返回结果四舍五入到 2 位小数；
    - 空列表返回 0.0。
    """
    # TODO: 实现总价计算
    raise NotImplementedError
