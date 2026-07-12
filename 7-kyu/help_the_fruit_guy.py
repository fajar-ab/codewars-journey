# Rank  : 7 kyu
# Title : Help the Fruit Guy
# Link  : https://www.codewars.com/kata/557af4c6169ac832300000ba

import re


def remove_rotten(bag_of_fruits):
    if bag_of_fruits:
        return [re.sub("rotten", "", word).lower() for word in bag_of_fruits]

    return []


print(
    remove_rotten(
        ["rottenApple", "rottenBanana", "rottenApple", "rottenPineapple", "rottenKiwi"]
    )
)
