# Rank  : 8 kyu
# Title : Are You Playing Banjo?
# Link  : https://www.codewars.com/kata/reviews/54a5cd6f8e5c31733e000013/groups/626e3668da0e2200017595da

def are_you_playing_banjo(name):
    return f"{name} plays banjo" if name.startswith(('R', 'r')) else f"{name} does not play banjo"
