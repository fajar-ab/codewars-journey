# Rank  : 7 kyu
# Title : Dictionary from two lists
# Link  : https://www.codewars.com/kata/5533c2a50c4fea6832000101


from itertools import zip_longest


def create_dict(keys, values):
    return {
        key: value
        for key, value in zip_longest(keys, values, fillvalue=None)
        if key is not None
    }
