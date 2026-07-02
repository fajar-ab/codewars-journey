# Rank  : 8 kyu
# Title : Exclamation marks series #1: Remove an exclamation mark from the end of string
# Link  : https://www.codewars.com/kata/57fae964d80daa229d000126


def remove(s):
    return s.removesuffix("!")


print(remove("!hello! hello!!!"))
