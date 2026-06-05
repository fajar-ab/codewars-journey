# Rank  : 8 kyu
# Title : Determine offspring sex based on genes XX and XY chromosomes
# Link  : https://www.codewars.com/kata/56530b444e831334c0000020


def chromosome_check(chromosome):
    return {
        "XY": "Congratulations! You're going to have a son.",
        "XX": "Congratulations! You're going to have a daughter.",
    }.get(chromosome)


assert chromosome_check("XY") == "Congratulations! You're going to have a son."
assert chromosome_check("XX") == "Congratulations! You're going to have a daughter."
