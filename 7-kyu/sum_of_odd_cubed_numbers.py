# Rank  : 7 kyu
# Title : Sum of Odd Cubed Numbers
# Link  : https://www.codewars.com/kata/580dda86c40fa6c45f00028a


def cube_odd(arr):
    if any(isinstance(el, (str, bool)) for el in arr):
        return None

    return sum(n for n in map(lambda x: x**3, arr) if n % 2 != 0)
