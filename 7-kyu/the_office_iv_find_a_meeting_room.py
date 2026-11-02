# Rank  : 7 kyu
# Title : The Office IV - Find a Meeting Room
# Link  : https://www.codewars.com/kata/57f604a21bd4fe771b00009c


def meeting(rooms):
    return "None available!" if "O" not in rooms else rooms.index("O")


print(meeting(["X", "O", "X"]), 1)
print(meeting(["O", "X", "X", "X", "X"]), 0)
print(meeting(["X", "X", "O", "X", "X"]), 2)
print(meeting(["X"]), "None available!")
