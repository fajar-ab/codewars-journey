# Rank  : 8 kyu
# Title : NBA full 48 minutes average
# Link  : https://www.codewars.com/kata/587c2d08bb65b5e8040004fd


def nba_extrap(ppg, mpg):
    return round((ppg / mpg) * 48, 1) if mpg != 0 else 0
