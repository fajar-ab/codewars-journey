# Rank  : 7 kyu
# Title : Functional Addition
# Link  : https://www.codewars.com/kata/538835ae443aae6e03000547


from typing import Callable


def add(n: int) -> Callable:
    return lambda x: x + n
