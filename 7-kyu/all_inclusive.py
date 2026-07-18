# Rank  : 7 kyu
# Title : All Inclusive?
# Link  : https://www.codewars.com/kata/5700c9acc1555755be00027e


def contain_all_rots(strng, arr):
    n = len(strng)
    return (
        len(
            [
                rots
                for rots in map(lambda i: strng[i:] + strng[:i], range(n))
                if rots in arr
            ]
        )
        == n
    )
