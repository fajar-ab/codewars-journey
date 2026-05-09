# Rank  : 7 kyu
# Title : Sum of the first nth term of Series
# Link  : https://www.codewars.com/kata/555eded1ad94b00403000071

def series_sum(n):
    return f"{sum(1 / (3 * i + 1) for i in range(n)):.2f}"
