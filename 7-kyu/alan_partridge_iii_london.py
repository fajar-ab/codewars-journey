# Rank  : 7 kyu
# Title : Alan Partridge III - London
# Link  : https://www.codewars.com/kata/580a41b6d6df740d6100030c


LIST_OF_STOPS = frozenset(
    {
        "Rejection",
        "Disappointment",
        "Backstabbing Central",
        "Shattered Dreams Parkway",
    }
)


def alan(arr):
    if LIST_OF_STOPS.issubset(arr):
        return "Smell my cheese you mother!"

    return "No, seriously, run. You will miss it."
