# Rank  : 8 kyu
# Title : Filter out the geese
# Link  : https://www.codewars.com/kata/57ee4a67108d3fd9eb0000e7

geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]


def goose_filter(birds):
    return filter(lambda item: item not in geese, birds)
