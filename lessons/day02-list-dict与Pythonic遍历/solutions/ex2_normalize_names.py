def normalize_names(names: list[str]) -> list[str]:
    result: list[str] = []
    for name in names:
        normalized = " ".join(name.strip().lower().split())
        if normalized:
            result.append(normalized)
    return result
