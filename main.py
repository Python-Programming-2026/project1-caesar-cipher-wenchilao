from cipher import encrypt, decrypt
from cracker import print_brute_force_results, auto_crack
from file_handler import encrypt_file, decrypt_file


def get_shift():
    """
    获取用户输入的位移量，并确保它是整数。
    """
    while True:
        shift_input = input("请输入位移量（整数）: ")
        try:
            return int(shift_input)
        except ValueError:
            print("输入无效，请输入整数。")


def encrypt_text():
    """
    处理文本加密功能。
    """
    text = input("请输入要加密的文本: ")
    shift = get_shift()
    result = encrypt(text, shift)
    print("\n加密结果：")
    print(result)


def decrypt_text():
    """
    处理文本解密功能。
    """
    text = input("请输入要解密的文本: ")
    shift = get_shift()
    result = decrypt(text, shift)
    print("\n解密结果：")
    print(result)


def brute_force_text():
    """
    处理暴力破解功能。
    """
    cipher_text = input("请输入要破解的密文: ")
    print_brute_force_results(cipher_text)


def auto_crack_text():
    """
    处理自动破译功能。
    """
    cipher_text = input("请输入要自动破译的密文: ")
    best_shift, best_result, best_chi_score, best_word_score = auto_crack(cipher_text)

    print("\n自动破译推荐结果：")
    print(f"推荐 shift: {best_shift}")
    print(f"推荐明文: {best_result}")
    print(f"字母频率评分: {best_chi_score:.4f}")
    print(f"单词匹配分数: {best_word_score}")


def encrypt_text_file():
    """
    处理文件加密功能。
    """
    input_path = input("请输入要加密的 txt 文件路径: ")
    output_path = input("请输入加密后输出文件路径: ")
    shift = get_shift()

    try:
        encrypt_file(input_path, output_path, shift)
        print("\n文件加密完成。")
        print(f"输出文件：{output_path}")
    except FileNotFoundError:
        print("输入文件不存在，请检查路径是否正确。")
    except Exception as error:
        print(f"发生错误：{error}")


def decrypt_text_file():
    """
    处理文件解密功能。
    """
    input_path = input("请输入要解密的 txt 文件路径: ")
    output_path = input("请输入解密后输出文件路径: ")
    shift = get_shift()

    try:
        decrypt_file(input_path, output_path, shift)
        print("\n文件解密完成。")
        print(f"输出文件：{output_path}")
    except FileNotFoundError:
        print("输入文件不存在，请检查路径是否正确。")
    except Exception as error:
        print(f"发生错误：{error}")


def show_menu():
    """
    显示主菜单。
    """
    print("\n====== 凯撒密码系统 ======")
    print("1. 文本加密")
    print("2. 文本解密")
    print("3. 暴力破解")
    print("4. 自动破译")
    print("5. 文件加密")
    print("6. 文件解密")
    print("0. 退出")
    print("=========================")


def main():
    """
    主程序入口。
    """
    while True:
        show_menu()
        choice = input("请输入功能编号: ")

        if choice == "1":
            encrypt_text()
        elif choice == "2":
            decrypt_text()
        elif choice == "3":
            brute_force_text()
        elif choice == "4":
            auto_crack_text()
        elif choice == "5":
            encrypt_text_file()
        elif choice == "6":
            decrypt_text_file()
        elif choice == "0":
            print("程序已退出。")
            break
        else:
            print("输入无效，请重新输入。")


if __name__ == "__main__":
    main()