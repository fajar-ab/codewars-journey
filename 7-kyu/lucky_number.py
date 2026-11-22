# Rank  : 7 kyu
# Title : lucky number
# Link  : https://www.codewars.com/kata/55afed09237df73343000042


def is_lucky(n):
    return sum(map(int, str(n))) % 9 == 0


print(is_lucky(0))
print(is_lucky(1892376))
print(is_lucky(189237))
