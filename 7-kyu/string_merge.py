# Rank  : 7 kyu
# Title : String Merge!
# Link  : https://www.codewars.com/kata/597bb84522bc93b71e00007e


def string_merge(string1, string2, letter):
    index1 = string1.index(letter)
    index2 = string2.index(letter)

    return string1[:index1] + string2[index2:]
