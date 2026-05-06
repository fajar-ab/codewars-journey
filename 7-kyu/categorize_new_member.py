# Rank  : 7 kyu
# Title : Categorize New Member
# Link  : https://www.codewars.com/kata/reviews/5502c9e8b3216ec63c0001ac/groups/69fb4e511558dbce4022df0f

def open_or_senior(data):
    return [["Open", "Senior"][all([age>=55, handicap>7])] for age, handicap in data]
