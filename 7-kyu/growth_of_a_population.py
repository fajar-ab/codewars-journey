# Rank  : 7 kyu
# Title : Growth of a Population
# Link  : https://www.codewars.com/kata/563b662a59afc2b5120000c6

def nb_year(p0, percent, aug, p):
    population = p0
    year = 0

    while population < p:
        year += 1
        population = int(population + population * (percent / 100) + aug)

    return year


print(nb_year(1500000, 0.0, 10000, 2000000))