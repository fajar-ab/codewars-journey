# Rank  : 6 kyu
# Title : Simple Encryption #1 - Alternating Split
# Link  : https://www.codewars.com/kata/57814d79a56c88e3e0000786


def decrypt(text, n):
    arr = list(text)

    for _ in range(n):
        result = [""] * len(arr)

        result[::2] = arr[len(arr) // 2 :]
        result[1::2] = arr[: len(arr) // 2]

        arr = result

    return "".join(arr)


def encrypt(text, n):
    arr = list(text)

    for _ in range(n):
        arr = arr[1::2] + arr[::2]

    return "".join(arr)


print(encrypt("01234", 2))
print(decrypt("32104", 2))
