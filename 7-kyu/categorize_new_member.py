# Rank  : 7 kyu
# Title : Categorize New Member
# Link  : https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa

def open_or_senior(data):
    return [["Open", "Senior"][all([age>=55, handicap>7])] for age, handicap in data]
