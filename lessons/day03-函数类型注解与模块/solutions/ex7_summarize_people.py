def extract_names(records: list[dict[str, object]]) -> list[str]:
    names: list[str] = []
    for record in records:
        name = record.get("name")
        if isinstance(name, str):
            names.append(name)
    return names


def count_by_field(records: list[dict[str, object]], field: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for record in records:
        value = record.get(field)
        if isinstance(value, str):
            counts[value] = counts.get(value, 0) + 1
    return counts


def summarize_people(records: list[dict[str, object]]) -> dict[str, object]:
    names = sorted(extract_names(records))
    return {
        "count": len(names),
        "names": names,
        "cities": count_by_field(records, "city"),
        "roles": count_by_field(records, "role"),
    }
