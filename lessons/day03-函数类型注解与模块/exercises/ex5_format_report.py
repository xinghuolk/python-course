def format_report(
    title: str,
    *lines: str,
    uppercase_title: bool = False,
) -> str:
    """生成简单文本报告。

    规则：
    - title 去掉首尾空白；
    - uppercase_title=True 时标题转大写；
    - lines 去空白后，空行丢弃；
    - 正文行按 "1. xxx"、"2. yyy" 编号；
    - 标题和正文用换行拼接；
    - 没有正文时只返回标题。
    """
    # TODO: 使用 *lines 接收多行正文
    raise NotImplementedError
