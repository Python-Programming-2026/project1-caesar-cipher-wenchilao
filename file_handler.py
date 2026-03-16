"""
file_handler.py
文件读写与文件加解密模块

功能：
1. 读取 txt 文件
2. 写入 txt 文件
3. 文件加密
4. 文件解密
"""

from cipher import encrypt, decrypt


def read_text_file(file_path: str) -> str:
    """
    读取文本文件内容。
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
        print(f"读取成功：{file_path}")
        return content
    except FileNotFoundError:
        print(f"错误：文件 {file_path} 未找到。")
        return ""


def write_text_file(file_path: str, content: str) -> None:
    """
    将内容写入文本文件。
    """
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)
        print(f"写入成功：{file_path}")
    except Exception as e:
        print(f"写入文件时发生错误: {e}")


def encrypt_file(input_path: str, output_path: str, shift: int) -> None:
    """
    读取输入文件，进行凯撒加密后写入输出文件。
    """
    text = read_text_file(input_path)
    if text:  # 只有在文件内容不为空时才加密
        encrypted_text = encrypt(text, shift)
        write_text_file(output_path, encrypted_text)


def decrypt_file(input_path: str, output_path: str, shift: int) -> None:
    """
    读取输入文件，进行凯撒解密后写入输出文件。
    """
    text = read_text_file(input_path)
    if text:  # 只有在文件内容不为空时才解密
        decrypted_text = decrypt(text, shift)
        write_text_file(output_path, decrypted_text)


if __name__ == "__main__":
    sample_input = "input.txt"
    sample_encrypted = "encrypted.txt"
    sample_decrypted = "decrypted.txt"
    sample_shift = 3

    try:
        encrypt_file(sample_input, sample_encrypted, sample_shift)
        print(f"加密完成：{sample_input} -> {sample_encrypted}")

        decrypt_file(sample_encrypted, sample_decrypted, sample_shift)
        print(f"解密完成：{sample_encrypted} -> {sample_decrypted}")
    except FileNotFoundError:
        print("测试文件不存在，请先创建 input.txt")