# Rank  : 7 kyu
# Title : makeBackronym
# Link  : https://www.codewars.com/kata/55805ab490c73741b7000064


# preloaded variable: "dictionary"
def make_backronym(acronym):
    return " ".join(dictionary[key] for key in acronym.upper())
