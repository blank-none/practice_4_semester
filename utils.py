ALPHABET = ",.:()-0123456789АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

def caesar_encrypt(text, shift):
    encrypted = ''
    for char in text:
        if char in ALPHABET:
            idx = (ALPHABET.index(char) + shift) % len(ALPHABET)
            encrypted += ALPHABET[idx]
        else:
            encrypted += char
    return encrypted

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def vigenere_encrypt(text, key):
    key = key.upper()
    key_length = len(key)
    key_as_int = [ALPHABET.index(char) for char in key]
    text_as_int = [ALPHABET.index(char) for char in text]
    encrypted = ''
    for i in range(len(text_as_int)):
        value = (text_as_int[i] + key_as_int[i % key_length]) % len(ALPHABET)
        encrypted += ALPHABET[value]
    return encrypted

def vigenere_decrypt(text, key):
    key = key.upper()
    key_length = len(key)
    key_as_int = [ALPHABET.index(char) for char in key]
    text_as_int = [ALPHABET.index(char) for char in text]
    decrypted = ''
    for i in range(len(text_as_int)):
        value = (text_as_int[i] - key_as_int[i % key_length]) % len(ALPHABET)
        decrypted += ALPHABET[value]
    return decrypted
