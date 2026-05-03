# Rank  : 8 kyu
# Title : Are You Playing Banjo?
# Link  : https://www.codewars.com/kata/53af2b8861023f1d88000832

def are_you_playing_banjo(name):
    return f"{name} plays banjo" if name.startswith(('R', 'r')) else f"{name} does not play banjo"
