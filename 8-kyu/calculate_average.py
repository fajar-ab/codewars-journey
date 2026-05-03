# Rank  : 8 kyu
# Title : Calculate average
# Link  : https://www.codewars.com/kata/57a2013acf1fa5bfc4000921

def find_average(numbers):
    if not numbers: return 0

    amount, lenght = 0, 0
    for number in numbers:
        amount, lenght = amount + number, lenght + 1
    
    average = amount / lenght

    return average
