def is_palindrome(s: str) -> bool:
    """判断 s 是否回文，忽略大小写与非字母数字字符。"""
    cleaned = ""
    for ch in s:
        if ch.isalnum():
            cleaned += ch.lower()
    return cleaned == cleaned[::-1]
