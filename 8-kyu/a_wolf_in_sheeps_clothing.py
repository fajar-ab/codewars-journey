# Rank  : 8 kyu
# Title : A wolf in sheep's clothing
# Link  : https://www.codewars.com/kata/5c8bfa44b9d1192e1ebd3d15


def warn_the_sheep(queue):
    worf_in = queue.index("wolf") + 1

    return (
        "Oi! Sheep number {}! You are about to be eaten by a wolf!".format(
            len(queue) - worf_in
        ),
        "Pls go away and stop eating my sheep",
    )[len(queue) == worf_in]
