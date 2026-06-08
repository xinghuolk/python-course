def word_frequencies(text: str) -> dict[str, int]:
    normalized_chars: list[str] = []
    for ch in text.lower():
        if ch.isalnum():
            normalized_chars.append(ch)
        else:
            normalized_chars.append(" ")

    counts: dict[str, int] = {}
    for word in "".join(normalized_chars).split():
        counts[word] = counts.get(word, 0) + 1
    return counts
