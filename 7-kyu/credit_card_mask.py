# Rank  : 7 kyu
# Title : Credit Card Mask
# URL   : https://www.codewars.com/kata/reviews/55772f4ae9be6616700000ef/groups/55781c9990505152b700006a

# return masked string
def maskify(cc):
    return "#" * (len(cc) -4) + cc[-4:]