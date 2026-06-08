def add_task(task: str, tasks: list[str] | None = None) -> list[str]:
    """返回添加任务后的新列表。

    规则：
    - tasks 默认为 None，表示从空列表开始；
    - task 去掉首尾空白；
    - task 为空时不添加；
    - 不修改传入的 tasks 列表。

    这个练习用于避免 `def add_task(task, tasks=[])` 这类可变默认参数坑。
    """
    # TODO: 用 None 作为默认空列表信号，并复制输入列表
    raise NotImplementedError
