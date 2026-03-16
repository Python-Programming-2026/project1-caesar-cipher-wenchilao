import gradio as gr
from cipher import encrypt, decrypt
from cracker import brute_force, auto_crack
from file_handler import encrypt_file, decrypt_file


def encrypt_text_interface(text, shift):
    try:
        shift = int(shift)
        return encrypt(text, shift)
    except Exception as error:
        return f"发生错误：{error}"


def decrypt_text_interface(text, shift):
    try:
        shift = int(shift)
        return decrypt(text, shift)
    except Exception as error:
        return f"发生错误：{error}"


def brute_force_interface(cipher_text):
    try:
        results = brute_force(cipher_text)
        output_lines = []
        for shift, result in results:
            output_lines.append(f"shift = {shift:2d} -> {result}")
        return "\n".join(output_lines)
    except Exception as error:
        return f"发生错误：{error}"


def auto_crack_interface(cipher_text):
    try:
        best_shift, best_result, best_chi_score, best_word_score = auto_crack(cipher_text)
        return (
            f"推荐 shift: {best_shift}\n"
            f"推荐明文: {best_result}\n"
            f"字母频率评分: {best_chi_score:.4f}\n"
            f"单词匹配分数: {best_word_score}"
        )
    except Exception as error:
        return f"发生错误：{error}"


def encrypt_file_interface(input_path, output_path, shift):
    try:
        shift = int(shift)
        encrypt_file(input_path, output_path, shift)
        return f"文件加密完成。\n输出文件：{output_path}"
    except FileNotFoundError:
        return "输入文件不存在，请检查路径是否正确。"
    except Exception as error:
        return f"发生错误：{error}"


def decrypt_file_interface(input_path, output_path, shift):
    try:
        shift = int(shift)
        decrypt_file(input_path, output_path, shift)
        return f"文件解密完成。\n输出文件：{output_path}"
    except FileNotFoundError:
        return "输入文件不存在，请检查路径是否正确。"
    except Exception as error:
        return f"发生错误：{error}"


with gr.Blocks(title="凯撒密码加解密与破译分析系统") as demo:
    gr.Markdown(
        """
        # 凯撒密码加解密与破译分析系统
        ## Caesar Cipher Encryption, Decryption and Cracking System

        本系统支持：
        - 文本加密
        - 文本解密
        - 暴力破解
        - 自动破译
        - 文件加密
        - 文件解密
        """
    )

    with gr.Tab("文本加密"):
        encrypt_input_text = gr.Textbox(
            label="请输入明文",
            placeholder="例如：Hello, World!"
        )
        encrypt_shift = gr.Number(label="请输入位移量 shift", value=3, precision=0)
        encrypt_output_text = gr.Textbox(label="加密结果", lines=4)
        encrypt_button = gr.Button("开始加密")
        encrypt_button.click(
            fn=encrypt_text_interface,
            inputs=[encrypt_input_text, encrypt_shift],
            outputs=encrypt_output_text
        )

    with gr.Tab("文本解密"):
        decrypt_input_text = gr.Textbox(
            label="请输入密文",
            placeholder="例如：Khoor, Zruog!"
        )
        decrypt_shift = gr.Number(label="请输入位移量 shift", value=3, precision=0)
        decrypt_output_text = gr.Textbox(label="解密结果", lines=4)
        decrypt_button = gr.Button("开始解密")
        decrypt_button.click(
            fn=decrypt_text_interface,
            inputs=[decrypt_input_text, decrypt_shift],
            outputs=decrypt_output_text
        )

    with gr.Tab("暴力破解"):
        brute_force_input = gr.Textbox(
            label="请输入要破解的密文",
            placeholder="例如：Khoor, Zruog!"
        )
        brute_force_output = gr.Textbox(label="暴力破解结果", lines=20)
        brute_force_button = gr.Button("开始暴力破解")
        brute_force_button.click(
            fn=brute_force_interface,
            inputs=brute_force_input,
            outputs=brute_force_output
        )

    with gr.Tab("自动破译"):
        auto_crack_input = gr.Textbox(
            label="请输入要自动破译的密文",
            placeholder="例如：Khoor, Zruog!"
        )
        auto_crack_output = gr.Textbox(label="自动破译推荐结果", lines=8)
        auto_crack_button = gr.Button("开始自动破译")
        auto_crack_button.click(
            fn=auto_crack_interface,
            inputs=auto_crack_input,
            outputs=auto_crack_output
        )

    with gr.Tab("文件加密"):
        file_encrypt_input_path = gr.Textbox(
            label="输入文件路径",
            placeholder="例如：input.txt"
        )
        file_encrypt_output_path = gr.Textbox(
            label="输出文件路径",
            placeholder="例如：encrypted.txt"
        )
        file_encrypt_shift = gr.Number(label="请输入位移量 shift", value=3, precision=0)
        file_encrypt_output = gr.Textbox(label="运行结果", lines=4)
        file_encrypt_button = gr.Button("开始文件加密")
        file_encrypt_button.click(
            fn=encrypt_file_interface,
            inputs=[file_encrypt_input_path, file_encrypt_output_path, file_encrypt_shift],
            outputs=file_encrypt_output
        )

    with gr.Tab("文件解密"):
        file_decrypt_input_path = gr.Textbox(
            label="输入文件路径",
            placeholder="例如：encrypted.txt"
        )
        file_decrypt_output_path = gr.Textbox(
            label="输出文件路径",
            placeholder="例如：decrypted.txt"
        )
        file_decrypt_shift = gr.Number(label="请输入位移量 shift", value=3, precision=0)
        file_decrypt_output = gr.Textbox(label="运行结果", lines=4)
        file_decrypt_button = gr.Button("开始文件解密")
        file_decrypt_button.click(
            fn=decrypt_file_interface,
            inputs=[file_decrypt_input_path, file_decrypt_output_path, file_decrypt_shift],
            outputs=file_decrypt_output
        )

if __name__ == "__main__":
    demo.launch()