def count_vowels(s: str) -> int:
    """统计 s 中元音字母的个数。"""
    count = 0
    for ch in s.lower():
        if ch in "aeiou":
            count += 1
    return count
