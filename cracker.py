"""
cracker.py
凯撒密码破解模块

功能：
1. 暴力破解：列出 1~25 所有位移结果
2. 自动破译：结合英文字母频率分析 + 常见英文单词匹配，推荐最可能结果
"""

from cipher import decrypt

# 英文字母常见频率（百分比）
ENGLISH_FREQ = {
    "a": 8.17, "b": 1.49, "c": 2.78, "d": 4.25, "e": 12.70,
    "f": 2.23, "g": 2.02, "h": 6.09, "i": 6.97, "j": 0.15,
    "k": 0.77, "l": 4.03, "m": 2.41, "n": 6.75, "o": 7.51,
    "p": 1.93, "q": 0.10, "r": 5.99, "s": 6.33, "t": 9.06,
    "u": 2.76, "v": 0.98, "w": 2.36, "x": 0.15, "y": 1.97,
    "z": 0.07
}

# 常见英文单词，可自行继续补充
COMMON_WORDS = {
    "hello", "world", "the", "and", "is", "this", "that", "python",
    "cipher", "caesar", "test", "text", "program", "example", "you",
    "he", "she", "it", "we", "they", "of", "to", "in", "on", "for"
}


def brute_force(cipher_text: str) -> list:
    """
    暴力破解凯撒密码，尝试所有 1~25 的位移量。
    返回格式: [(shift, result), ...]
    """
    if not isinstance(cipher_text, str):
        raise TypeError("cipher_text 必须是字符串。")

    results = []
    for shift in range(1, 26):
        result = decrypt(cipher_text, shift)
        results.append((shift, result))
    return results


def count_letters(text: str) -> dict:
    """
    统计文本中 26 个字母出现次数。
    """
    counts = {chr(i): 0 for i in range(ord("a"), ord("z") + 1)}

    for ch in text.lower():
        if "a" <= ch <= "z":
            counts[ch] += 1

    return counts


def chi_squared_score(text: str) -> float:
    """
    使用卡方统计量评估文本与正常英文频率的接近程度。
    分数越小，越像正常英文。
    """
    counts = count_letters(text)
    total_letters = sum(counts.values())

    if total_letters == 0:
        return float("inf")

    score = 0.0
    for letter, expected_freq in ENGLISH_FREQ.items():
        observed = counts[letter]
        expected = total_letters * (expected_freq / 100)
        score += ((observed - expected) ** 2) / expected

    return score


def word_match_score(text: str) -> int:
    """
    统计文本中匹配到的常见英文单词数量。
    分数越高，越可能是正常英文。
    """
    words = text.lower().replace(",", " ").replace(".", " ").replace("!", " ") \
        .replace("?", " ").replace(":", " ").replace(";", " ").split()

    score = 0
    for word in words:
        if word in COMMON_WORDS:
            score += 1
    return score


def auto_crack(cipher_text: str) -> tuple:
    """
    自动破译凯撒密码。
    结合：
    1. 单词匹配分数（越高越好）
    2. 字母频率卡方分数（越低越好）

    返回:
        (best_shift, best_result, best_chi_score, best_word_score)
    """
    if not isinstance(cipher_text, str):
        raise TypeError("cipher_text 必须是字符串。")

    candidates = brute_force(cipher_text)

    best_shift = None
    best_result = ""
    best_chi_score = float("inf")
    best_word_score = -1

    for shift, result in candidates:
        current_word_score = word_match_score(result)
        current_chi_score = chi_squared_score(result)

        # 先比较单词匹配分数，再比较字母频率分数
        if current_word_score > best_word_score:
            best_word_score = current_word_score
            best_chi_score = current_chi_score
            best_shift = shift
            best_result = result
        elif current_word_score == best_word_score and current_chi_score < best_chi_score:
            best_chi_score = current_chi_score
            best_shift = shift
            best_result = result

    return best_shift, best_result, best_chi_score, best_word_score


def print_brute_force_results(cipher_text: str) -> None:
    """
    以更清晰的格式打印暴力破解结果。
    """
    results = brute_force(cipher_text)
    print("\n暴力破解结果：")
    print("-" * 40)
    for shift, result in results:
        print(f"shift = {shift:2d} -> {result}")
    print("-" * 40)


if __name__ == "__main__":
    sample_cipher = "Khoor, Zruog!"

    print("测试密文：", sample_cipher)

    print_brute_force_results(sample_cipher)

    best_shift, best_result, best_chi_score, best_word_score = auto_crack(sample_cipher)

    print("\n自动破译推荐结果：")
    print(f"推荐 shift: {best_shift}")
    print(f"推荐明文: {best_result}")
    print(f"字母频率评分: {best_chi_score:.4f}")
    print(f"单词匹配分数: {best_word_score}")