# Rank  : 8 kyu
# Title : I love you, a little , a lot, passionately ... not at all
# Link  : https://www.codewars.com/kata/57f24e6a18e9fad8eb000296


def how_much_i_love_you(nb_petals):
    return ("I love you", "a little", "a lot", "passionately", "madly", "not at all")[
        (nb_petals - 1) % 6
    ]


assert how_much_i_love_you(7) == "I love you"
assert how_much_i_love_you(3) == "a lot"
assert how_much_i_love_you(6) == "not at all"
