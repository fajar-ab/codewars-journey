# Rank  : 8 kyu
# Title : Netralisasi
# Link  : https://www.codewars.com/kata/65128732b5aff40032a3d8f0


def neutralise(s1, s2):
    return "".join(
        "+" if a == b == "+" else "-" if a == b == "-" else "0" for a, b in zip(s1, s2)
    )
