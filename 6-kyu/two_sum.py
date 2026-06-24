# Rank  : 6 kyu
# Title : Two Sum
# Link  : https://www.codewars.com/kata/52c31f8e6605bcc646000082


def two_sum(numbers, target):
    seen = {}

    for index, num in enumerate(numbers):
        selisih = target - num

        if selisih in seen:
            return (seen[selisih], index)

        seen[num] = index


print(two_sum([1234, 5678, 9012], 14690))
