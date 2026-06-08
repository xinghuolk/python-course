def build_user_profile(
    name: str,
    email: str | None = None,
    **extra: object,
) -> dict[str, object]:
    """构造用户资料 dict。

    规则：
    - name 去掉首尾空白；
    - email 为 None 时保留 None，否则去空白并转小写；
    - extra 里的键值合并进结果；
    - extra 中值为 None 的字段忽略。

    示例：build_user_profile(" Alice ", role="admin")
    -> {"name": "Alice", "email": None, "role": "admin"}
    """
    # TODO: 使用 **extra 处理额外字段
    raise NotImplementedError
