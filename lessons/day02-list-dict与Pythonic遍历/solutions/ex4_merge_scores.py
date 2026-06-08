def merge_scores(names: list[str], scores: list[int]) -> dict[str, int]:
    return {name: score for name, score in zip(names, scores)}
