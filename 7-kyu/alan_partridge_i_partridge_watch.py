# Rank  : 7 kyu
# Title : Alan Partridge I - Partridge Watch
# Link  : https://www.codewars.com/kata/5808c8eff0ed4210de000008


RELATE_TERMS = {
    "Partridge",
    "PearTree",
    "Chat",
    "Dan",
    "Toblerone",
    "Lynn",
    "AlphaPapa",
    "Nomad",
}


def part(arr):
    sum_terms = sum(1 for term in arr if term in RELATE_TERMS)

    return (
        f"Mine's a Pint{'!' * sum_terms}"
        if sum_terms
        else "Lynn, I've pierced my foot on a spike!!"
    )
