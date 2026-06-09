def format_table(rows: list[tuple[str, int]]) -> str:
    """把 (name, count) 列表格式化成对齐的表格字符串。"""
    if not rows:
        return ""
    width = max(len(name) for name, _ in rows)
    return "\n".join(f"{name:<{width}}: {count}" for name, count in rows)
