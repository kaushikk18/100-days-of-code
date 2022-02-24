def caesar_cipher_converter(txt, shift):
    ciphered_text = ''

    for i in range(len(txt)):
        char = txt[i]

        if char.isupper():
            ciphered_text += chr((ord(char)+shift-65) % 26+65)

        if char.islower():
            ciphered_text += chr((ord(char)+shift-97) % 26+97)

    print(ciphered_text)


txt = 'hello peter'
shift = 4
caesar_cipher_converter(txt, shift)
