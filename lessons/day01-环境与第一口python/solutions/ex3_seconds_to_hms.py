def seconds_to_hms(total: int) -> str:
    """把总秒数转成 "H:MM:SS"。"""
    minutes, seconds = divmod(total, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{hours}:{minutes:02d}:{seconds:02d}"
