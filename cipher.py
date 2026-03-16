"""
cipher.py
凯撒密码核心算法模块

功能：
1. 对文本进行加密
2. 对文本进行解密
3. 保留大小写
4. 非字母字符原样保留
"""

from string import ascii_lowercase, ascii_uppercase


def shift_char(ch: str, shift: int) -> str:
    """
    对单个字符进行凯撒位移。

    参数:
        ch (str): 单个字符
        shift (int): 位移量，可正可负

    返回:
        str: 位移后的字符
    """
    if len(ch) != 1:
        raise ValueError("shift_char 函数一次只能处理一个字符。")

    shift = shift % 26

    if ch in ascii_lowercase:
        old_index = ascii_lowercase.index(ch)
        new_index = (old_index + shift) % 26
        return ascii_lowercase[new_index]

    if ch in ascii_uppercase:
        old_index = ascii_uppercase.index(ch)
        new_index = (old_index + shift) % 26
        return ascii_uppercase[new_index]

    return ch


def encrypt(text: str, shift: int) -> str:
    """
    使用凯撒密码对文本进行加密。

    参数:
        text (str): 明文文本
        shift (int): 位移量

    返回:
        str: 加密后的密文
    """
    if not isinstance(text, str):
        raise TypeError("text 必须是字符串类型。")

    if not isinstance(shift, int):
        raise TypeError("shift 必须是整数类型。")

    encrypted_text = "".join(shift_char(ch, shift) for ch in text)
    return encrypted_text


def decrypt(text: str, shift: int) -> str:
    """
    使用凯撒密码对文本进行解密。

    参数:
        text (str): 密文文本
        shift (int): 位移量

    返回:
        str: 解密后的明文
    """
    if not isinstance(text, str):
        raise TypeError("text 必须是字符串类型。")

    if not isinstance(shift, int):
        raise TypeError("shift 必须是整数类型。")

    decrypted_text = "".join(shift_char(ch, -shift) for ch in text)
    return decrypted_text


if __name__ == "__main__":
    sample_text = "Hello, World!"
    sample_shift = 3

    encrypted = encrypt(sample_text, sample_shift)
    decrypted = decrypt(encrypted, sample_shift)

    print("原文：", sample_text)
    print("加密：", encrypted)
    print("解密：", decrypted)