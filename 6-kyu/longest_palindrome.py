# Rank  : 6 kyu
# Title : longest_palindrome
# Link  : https://www.codewars.com/kata/54bb6f887e5a80180900046b


def longest_palindrome(s):
    palindrome = []

    for i in range(len(s)):
        for j in range(i, len(s) + 1):
            if (potongan := s[i:j]) == potongan[::-1]:
                palindrome.append(len(s[i:j]))

    return max(palindrome, default=0)


print(longest_palindrome("aa"))
print(longest_palindrome("zzbaabcd"))
