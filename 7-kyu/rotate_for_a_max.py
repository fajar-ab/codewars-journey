# Rank  : 7 kyu
# Title : Rotate for a Max
# Link  : https://www.codewars.com/kata/56a4872cbb65f3a610000026


def max_rot(n):
    digits = list(str(n))
    k = len(digits)
    candidates = [n]

    for i in range(k - 1):
        segment = digits[i:]
        rotated = segment[1:] + segment[:1]
        digits = digits[:i] + rotated
        candidates.append(int("".join(digits)))

    return max(candidates)
