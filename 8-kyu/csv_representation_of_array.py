# Rank  : 8 kyu
# Title : CSV representation of array
# Link  : https://www.codewars.com/kata/5a34af40e1ce0eb1f5000036


def to_csv_text(array):
    return "\n".join(",".join(map(str, value)) for value in array)
