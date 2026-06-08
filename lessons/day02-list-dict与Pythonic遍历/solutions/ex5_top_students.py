def top_students(records: list[dict[str, object]], threshold: int) -> list[str]:
    result: list[str] = []
    for record in records:
        name = record.get("name")
        score = record.get("score")
        if isinstance(name, str) and isinstance(score, int) and score >= threshold:
            result.append(name)
    return result
