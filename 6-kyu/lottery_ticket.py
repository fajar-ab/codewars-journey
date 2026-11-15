# Rank  : 6 kyu
# Title : Lottery Ticket
# Link  : https://www.codewars.com/kata/57f625992f4d53c24200070e


def bingo(ticket, win):
    mini_wins = sum(1 for code, number in ticket if any(ord(c) == number for c in code))
    return "Winner!" if mini_wins >= win else "Loser!"


print(bingo([["ABC", 65], ["HGR", 74], ["BYHT", 74]], 2))
