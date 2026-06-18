# Rank  : 8 kyu
# Title : Pillars
# Link  : https://www.codewars.com/kata/5bb0c58f484fcd170700063d


def pillars(num_pill, dist, width):
    return (
        0 if num_pill == 1 else ((num_pill - 1) * dist * 100) + (num_pill - 2) * width
    )
