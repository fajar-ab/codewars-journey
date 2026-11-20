# Rank  : 6 kyu
# Title : Kebabize
# Link  : https://www.codewars.com/kata/57f8ff867a28db569e000c4a


def kebabize(st):
    return "".join(
        f"-{c.lower()}" if c.isupper() else c for c in st if not c.isdigit()
    ).lstrip("-")


print(kebabize("CamelsHave3ThreeHumps"))
