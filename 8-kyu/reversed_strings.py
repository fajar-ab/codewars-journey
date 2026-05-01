# Rank  : 8 kyu
# Title : Reversed Strings
# Link  : https://www.codewars.com/kata/reviews/54e10e357775b79e2800011c/groups/69f4fb7d8e340a5ce5a621dd

def solution(string):
    # return string[::-1]
    return "".join([string[i] for i in range(len(string)-1, -1, -1)])