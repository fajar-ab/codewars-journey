# Rank  : 6 kyu
# Title : +1 Array
# Link  : https://www.codewars.com/kata/5514e5b77e6b2f38e0000ca9


def up_array(arr):
    if not arr or not all(0 <= n <= 9 for n in arr):
        return None

    for i in reversed(range(len(arr))):
        if arr[i] == 9:
            arr[i] = 0
        else:
            arr[i] += 1
            break
    else:
        arr.insert(0, 1)

    return arr
