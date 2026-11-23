# Rank  : 7 kyu
# Title : Arithmetic progression
# Link  : https://www.codewars.com/kata/55caf1fd8063ddfa8e000018


from itertools import count, islice


def arithmetic_sequence_elements(a, d, n):
    return ", ".join(map(str, (islice(count(a, d), n))))


print(arithmetic_sequence_elements(1, 2, 5))
