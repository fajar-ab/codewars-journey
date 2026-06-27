# Rank  : 8 kyu
# Title : Is it a palindrome?
# Link  : https://www.codewars.com/kata/57a1fd2ce298a731b20006a4


def is_palindrome(s):
    s = s.casefold()
    return s == s[::-1]
