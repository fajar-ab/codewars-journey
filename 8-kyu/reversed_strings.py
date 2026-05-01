# Rank  : 8 kyu
# Title : Reversed Strings
# Link  : https://www.codewars.com/kata/5168bb5dfe9a00b126000018

def solution(string):
    # return string[::-1]
    return "".join([string[i] for i in range(len(string)-1, -1, -1)])