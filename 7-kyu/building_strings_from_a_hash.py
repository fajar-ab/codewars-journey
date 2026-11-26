# Rank  : 7 kyu
# Title : Building Strings From a Hash
# Link  : https://www.codewars.com/kata/51c7d8268a35b6b8b40002f2


def solution(pairs):
    return ",".join(f"{key} = {value}" for key, value in pairs.items())
