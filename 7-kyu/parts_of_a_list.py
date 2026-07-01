# Rank  : 7 kyu
# Title : Parts of a list
# Link  : https://www.codewars.com/kata/56f3a1e899b386da78000732


def partlist(arr):
    return [(" ".join(arr[:i]), " ".join(arr[i:])) for i in range(1, len(arr))]


print(partlist(["I", "wish", "I", "hadn't", "come"]))
