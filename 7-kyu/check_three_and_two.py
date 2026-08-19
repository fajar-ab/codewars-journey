# Rank  : 7 kyu
# Title : Check three and two
# Link  : https://www.codewars.com/kata/5a9e86705ee396d6be000091/train/python


def check_three_and_two(array):
    return all(2 <= array.count(v) <= 3 for v in set(array))


print(check_three_and_two(["a", "a", "a", "b", "b"]))
print(check_three_and_two(["a", "c", "a", "c", "b"]))
print(check_three_and_two(["a", "a", "a", "a", "a"]))
