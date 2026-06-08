def top_students(records: list[dict[str, object]], threshold: int) -> list[str]:
    result: list[tuple[str, float]] = []
    for record in records:
        name = record.get("name")
        score = record.get("score")
        if isinstance(name, str) and isinstance(score, int | float) and score >= threshold:
            result.append((name, float(score)))

    sorted_result = sorted(result, key=lambda item: item[1], reverse=True)
    return [name for name, _score in sorted_result]
