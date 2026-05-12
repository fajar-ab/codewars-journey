# Rank  : 7 kyu
# Title : Number of Folds
# Link  : https://www.codewars.com/kata/59cfe5b023daccfd07000048

def number_of_folds(n):
    grid, fold = 1, 0

    while grid < n:
        grid, fold = grid * 2, fold + 1
        
    return fold
