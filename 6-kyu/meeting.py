# Rank  : 6 kyu
# Title : Meeting
# Link  : https://www.codewars.com/kata/59df2f8f08c6cec835000012


def meeting(s):
    names = sorted(
        [a.upper().split(":") for a in s.split(";")], key=lambda x: (x[1], x[0])
    )
    return "".join(f"({last}, {first})" for first, last in names)


print(
    meeting(
        "Anna:Wahl;Grace:Gates;James:Russell;Elizabeth:Rudd;Victoria:STAN;Jacob:Wahl;Alex:Wahl;Antony:Gates;Alissa:Meta;Megan:Bell;Amandy:Stan;Anna:Steve"
    )
)
