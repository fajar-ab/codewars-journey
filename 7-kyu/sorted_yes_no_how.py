# Rank  : 7 kyu
# Title : Sorted? yes? no? how?
# Link  : https://www.codewars.com/kata/580a4734d6df748060000045


def is_sorted_and_how(arr):
    return (
        "yes, descending"
        if arr == sorted(arr, reverse=True)
        else "yes, ascending"
        if arr == sorted(arr)
        else "no"
    )
