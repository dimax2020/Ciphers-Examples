alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' \
           'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' \
           '123567890 _'


def encrypt_cipher(message: str, step: int) -> str:
    message = message.upper()
    cipher_text = ''
    for symbol in message:
        symbol_number = alphabet.find(symbol)
        if symbol_number != -1:
            cipher_text += alphabet[(symbol_number + step) % len(alphabet)]
        else:
            return f"Can't find symbol: {symbol}"
    return cipher_text


def decrypt_cipher(cipher_text: str, step: int) -> str:
    message = ''
    for symbol in cipher_text:
        symbol_number = alphabet.find(symbol)
        if symbol_number != -1:
            message += alphabet[(symbol_number - step) % len(alphabet)]
        else:
            return f"Can't find symbol: decode error"
    return message


if __name__ == '__main__':
    text = "I go for a walk Я иду гулять "
    step = 5

    cipher_text = encrypt_cipher(text, step)
    print("Encoded message:", cipher_text)

    message = decrypt_cipher(cipher_text, step)
    print("Decoded cipher:", message)
