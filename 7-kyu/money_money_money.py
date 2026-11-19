# Rank  : 7 kyu
# Title : Money, Money, Money
# Link  : https://www.codewars.com/kata/563f037412e5ada593000114


def calculate_years(saldo, bunga, pajak, target):
    tahun = 0

    while saldo < target:
        bunga_bersih = saldo * bunga * (1 - pajak)
        saldo = saldo + bunga_bersih
        tahun += 1

    return tahun


print(calculate_years(1000, 0.05, 0.18, 1100))
