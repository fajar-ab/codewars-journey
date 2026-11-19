# Rank  : 8 kyu
# Title : Are there any arrows left?
# Link  : https://www.codewars.com/kata/559f860f8c0d6c7784000119


def any_arrows(arrows):
    return any(not arrow.get("damaged", False) for arrow in arrows)
