def parse_tags(
    raw: str,
    *,
    normalize: bool = True,
    unique: bool = True,
) -> list[str]:
    tags: list[str] = []
    seen: set[str] = set()

    for part in raw.split(","):
        tag = part.strip()
        if normalize:
            tag = tag.lower()
        if not tag:
            continue
        if unique and tag in seen:
            continue
        seen.add(tag)
        tags.append(tag)

    return tags
