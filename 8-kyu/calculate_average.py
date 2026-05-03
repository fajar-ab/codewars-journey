# Rank  : 8 kyu
# Title : Calculate average
# Link  : https://www.codewars.com/kata/reviews/5865756e02698c83e60006d8/groups/69f72be46e466d77bf822bc0

def find_average(numbers):
    if not numbers: return 0

    amount, lenght = 0, 0
    for number in numbers:
        amount, lenght = amount + number, lenght + 1
    
    average = amount / lenght

    return average
