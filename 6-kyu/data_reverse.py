# Rank  : 6 kyu
# Title : Data Reverse
# Link  : https://www.codewars.com/kata/569d488d61b812a0f7000015


from itertools import batched, chain


def data_reverse(data):
    return list(chain.from_iterable(reversed(list(batched(data, 8)))))
