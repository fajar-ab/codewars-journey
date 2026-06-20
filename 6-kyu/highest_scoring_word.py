# Rank  : 6 kyu
# Title : Highest Scoring Word
# Link  : https://www.codewars.com/kata/57eb8fcdf670e99d9b000272


def high(x):
    points_word = dict(
        (word, sum(map(lambda c: ord(c) - 96, word))) for word in x.split()
    )

    return max(points_word, key=points_word.get)


print(high("aa b"))
print(high("b aa"))
