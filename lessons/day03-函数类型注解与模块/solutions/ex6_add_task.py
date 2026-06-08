def add_task(task: str, tasks: list[str] | None = None) -> list[str]:
    result = [] if tasks is None else tasks.copy()
    clean_task = task.strip()
    if clean_task:
        result.append(clean_task)
    return result
