# Rank  : 7 kyu
# Title : Count the Digit
# Link  : https://www.codewars.com/kata/566fc12495810954b1000030

def nb_dig(n, d):
    square = [k ** 2 for k in range(n+1)]
    resutl = "".join(map(str, square))

    return resutl.count(str(d))

print(nb_dig(5, 2))
print(nb_dig(5750, 0))
print(nb_dig(11011, 2))
print(nb_dig(12224, 8))
