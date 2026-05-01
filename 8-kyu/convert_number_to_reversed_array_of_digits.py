# Rank  : 8 kyu
# Title : Convert number to reversed array of digits
# Link  : https://www.codewars.com/kata/5583090cbe83f4fd8c000051

def digitize(number):
    return list(map(int, [n for n in str(number)[::-1]]))
