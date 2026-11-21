# Rank  : 6 kyu
# Title : longest_palindrome
# Link  : https://www.codewars.com/kata/54bb6f887e5a80180900046b


from itertools import combinations


def longest_palindrome(s):
    return max(
        (
            len(substring)
            for i, j in combinations(range(len(s) + 1), 2)
            if (substring := s[i:j]) == substring[::-1]
        ),
        default=0,
    )


print(longest_palindrome(""))
print(longest_palindrome("a"))
print(longest_palindrome("aa"))
print(longest_palindrome("zzbaabcd"))
