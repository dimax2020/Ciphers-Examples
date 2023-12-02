alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' \
           'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' \
           '123567890 _'


def egcd(a, b):
    gcd = 1
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b,a, x,y, u,v = a,r, u,v, m,n
        gcd = b
    return gcd, x, y


def modinv(a, m):
  gcd, x, y = egcd(a, m)
  if gcd != 1:
    return None
  else:
    return x % m

def encrypt_cipher(message: str, key: []) -> str:
    message = message.upper()
    cipher_text = ''
    for symbol in message:
        symbol_number = alphabet.find(symbol)
        if symbol_number != -1:
            cipher_text += alphabet[(symbol_number * key[0] + key[1]) % len(alphabet)]
        else:
            return f"Can't find symbol: {symbol}"
    return cipher_text


def decrypt_cipher(cipher_text: str, key: []) -> str:
    message = ''
    for symbol in cipher_text:
        symbol_number = alphabet.find(symbol)
        if symbol_number != -1:
            message += alphabet[(modinv(key[0], len(alphabet)) * (symbol_number - key[1])) % len(alphabet)]
        else:
            return f"Can't find symbol: decode error"
    return message


if __name__ == '__main__':
    text = "I go for a walk Я иду гулять "
    key = [17, 20]

    cipher_text = encrypt_cipher(text, key)
    print("Encoded message:", cipher_text)

    message = decrypt_cipher(cipher_text, key)
    print("Decoded cipher:", message)
