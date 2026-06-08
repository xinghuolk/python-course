def extract_names(records: list[dict[str, object]]) -> list[str]:
    """提取有效 name 字段，忽略缺失或非字符串 name。"""
    # TODO: 实现 helper 函数
    raise NotImplementedError


def count_by_field(records: list[dict[str, object]], field: str) -> dict[str, int]:
    """按字段统计频次，只统计值为字符串的字段。"""
    # TODO: 实现 helper 函数
    raise NotImplementedError


def summarize_people(records: list[dict[str, object]]) -> dict[str, object]:
    """汇总人员记录。

    records 元素示例：
    {"name": "Alice", "city": "Shanghai", "role": "admin"}

    返回：
    {
        "count": 有效 name 数量,
        "names": 按字母序排序的 name 列表,
        "cities": 按 city 统计的 dict,
        "roles": 按 role 统计的 dict
    }

    要求：主函数调用上面的 helper 函数完成工作。
    """
    # TODO: 组合 helper 函数
    raise NotImplementedError
