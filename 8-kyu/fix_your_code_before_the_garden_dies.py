# Rank  : 8 kyu
# Title : Fix your code before the garden dies!
# Link  : https://www.codewars.com/kata/57158fb92ad763bb180004e7


def rain_amount(mm):
    if (rain_amount := mm) < 40:
        return f"You need to give your plant {40 - rain_amount}mm of water"
    else:
        return "Your plant has had more than enough water for today!"
