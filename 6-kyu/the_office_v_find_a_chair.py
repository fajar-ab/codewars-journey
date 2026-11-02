# Rank  : 6 kyu
# Title : The Office V - Find a Chair
# Link  : https://www.codewars.com/kata/57f6051c3ff02f3b7300008b


def meeting(rooms, need):
    if not need:
        return "Game On"

    hasil = []

    for orang, kursi in rooms:
        cadangan = max(0, kursi - len(orang))
        ambil = min(cadangan, need)
        hasil.append(ambil)
        need -= ambil
        if need == 0:
            return hasil

    return "Not enough!"


print(meeting([["XXX", 3], ["XXXXX", 6], ["XXXXXX", 9]], 4), [0, 1, 3])
print(
    meeting(
        [["XXX", 1], ["XXXXXX", 6], ["X", 2], ["XXXXXX", 8], ["X", 3], ["XXX", 1]], 5
    ),
    [0, 0, 1, 2, 2],
)
print(meeting([["XX", 2], ["XXXX", 6], ["XXXXX", 4]], 0), "Game On")
print(meeting([["XX", 2], ["XXXX", 6], ["XXXXX", 4]], 8), "Not enough!")
