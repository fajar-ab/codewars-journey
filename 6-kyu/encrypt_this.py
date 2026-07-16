# Rank  : 6 kyu
# Title : Encrypt this!
# Link  : https://www.codewars.com/kata/5848565e273af816fb000449


def encrypt_this(text):
    encrypt = []

    for word in text.split():
        match list(word):
            case [first]:
                encrypt.append(f"{ord(first)}")
            case [first, last]:
                encrypt.append(f"{ord(first)}{last}")
            case [first, second, last]:
                encrypt.append(f"{ord(first)}{last}{second}")
            case [first, second, *other, last]:
                encrypt.append(f"{ord(first)}{last}{''.join(other)}{second}")

    return " ".join(encrypt)


print(encrypt_this("A wise old owl lived in an oak"))
print("65 119esi 111dl 111lw 108dvei 105n 97n 111ka")
