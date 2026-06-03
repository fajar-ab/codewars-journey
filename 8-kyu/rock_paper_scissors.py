# Rank  : 8 kyu
# Title : Rock Paper Scissors!
# Link  : https://www.codewars.com/kata/5672a98bdbdd995fad00000f

def rps(p1, p2):
    beats = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
    
    if p1 == p2:
        return "Draw!"
    
    if beats[p1] == p2:
        return "Player 1 won!"
    
    return "Player 2 won!"
