# Rank  : 7 kyu
# Title : Isograms
# Link  : https://www.codewars.com/kata/reviews/553a8421f3cc94444200007b/groups/553a907bcfc2484eb50000dc

def is_isogram(string):    
    return len(string) == len(set(string.lower()))

