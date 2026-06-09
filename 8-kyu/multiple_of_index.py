# Rank  : 8 kyu
# Title : Multiple of index
# Link  : https://www.codewars.com/kata/5a34b80155519e1a00000009


def multiple_of_index(arr):
    return [
        value
        for index, value in enumerate(arr)
        if (index == 0 and value == 0) or (index != 0 and value % index == 0)
    ]


print(multiple_of_index([22, -6, 32, 82, 9, 25]))
print(multiple_of_index([0, 2, 3, 6, 9]))
