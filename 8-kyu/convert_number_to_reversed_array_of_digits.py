# Rank  : 8 kyu
# Title : Convert number to reversed array of digits
# Link  : https://www.codewars.com/kata/reviews/55872716e678de23d40000bb/groups/69f504e88e340a5ce5a62285

def digitize(number):
    return list(map(int, [n for n in str(number)[::-1]]))
