# Rank  : 8 kyu
# Title : Count by X
# Link  : https://www.codewars.com/kata/reviews/551609a119aab6c5240000b5/groups/61d95fe5b7cf9b00016d557d

def count_by(x, n):
    return list(range(x, n * x + 1, x))
