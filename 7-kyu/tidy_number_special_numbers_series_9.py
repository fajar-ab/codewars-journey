# Rank  : 7 kyu
# Title : Tidy Number (Special Numbers Series #9)
# Link  : https://www.codewars.com/kata/5a87449ab1710171300000fd


def tidyNumber(n):
    return list(str(n)) == sorted(str(n))


print(tidyNumber(12))
