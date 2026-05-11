# Rank  : 7 kyu
# Title : Count the divisors of a number
# Link  : https://www.codewars.com/kata/542c0f198e077084c0000c2e

def divisors(n):
    return len([num for num in range(1, n+1) if n % num == 0])
