def build_user_profile(
    name: str,
    email: str | None = None,
    **extra: object,
) -> dict[str, object]:
    profile: dict[str, object] = {
        "name": name.strip(),
        "email": None if email is None else email.strip().lower(),
    }
    for key, value in extra.items():
        if value is not None:
            profile[key] = value
    return profile
