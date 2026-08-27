# Rank  : 7 kyu
# Title : Find Count of Most Frequent Item in an Array
# Link  : https://www.codewars.com/kata/56582133c932d8239900002e


def most_frequent_item_count(collection):
    return max([collection.count(el) for el in set(collection)], default=0)
