def generate_vigenere_table():
    table = []
    for i in range(33):
        row = [(chr(((i + j) % 33) + ord('А'))) for j in range(33)]
        table.append(row)
    return table


def vigenere_encrypt(plain_text, key):
    encrypted_text = []

    key = key.upper().replace('Ё', 'Е')
    plain_text = plain_text.upper().replace('Ё', 'Е')

    key_length = len(key)
    key_as_int = [ord(i) - ord('А') for i in key]
    plain_text_int = [ord(i) - ord('А') for i in plain_text]

    for i in range(len(plain_text_int)):
        if plain_text[i].isalpha():
            value = (plain_text_int[i] + key_as_int[i % key_length]) % 33
            encrypted_text.append(chr(value + ord('А')))
        else:
            encrypted_text.append(plain_text[i])

    return "".join(encrypted_text)



text = input("Введите текст: ")
key = input("Введите ключ: ")

encrypted = vigenere_encrypt(text, key)
print(f"Text: {text}")
print(f"Key: {key}")
print(f"Encrypted: {encrypted}")