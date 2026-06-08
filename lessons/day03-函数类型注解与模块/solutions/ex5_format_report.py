def format_report(
    title: str,
    *lines: str,
    uppercase_title: bool = False,
) -> str:
    clean_title = title.strip()
    if uppercase_title:
        clean_title = clean_title.upper()

    body = [line.strip() for line in lines if line.strip()]
    if not body:
        return clean_title

    numbered = [f"{index}. {line}" for index, line in enumerate(body, start=1)]
    return "\n".join([clean_title, *numbered])
