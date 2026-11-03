# Rank  : 7 kyu
# Title : Last Survivor
# Link  : https://www.codewars.com/kata/609eee71109f860006c377d1


def last_survivor(letters, coords):
    letters = list(letters)
    for index in coords:
        letters.pop(index)

    return "".join(letters)


print(last_survivor("abc", []))
