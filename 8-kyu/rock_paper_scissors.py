# Rank  : 8 kyu
# Title : Rock Paper Scissors!
# Link  : https://www.codewars.com/kata/5672a98bdbdd995fad00000f

def rps(p1, p2):
    beats = {"rock": 0, "paper": 1, "scissors": 2}
    result = ['Draw!', 'Player 1 won!', 'Player 2 won!']
    
    return result[beats[p1] - beats[p2]]
