# Rank  : 8 kyu
# Title : altERnaTIng cAsE <=> ALTerNAtiNG CaSe
# Link  : https://www.codewars.com/kata/56efc695740d30f963000557


def to_alternating_case(string):
    result = ""

    for alfa in string:
        if alfa.isupper():
            result += alfa.lower()
        elif alfa.islower():
            result += alfa.upper()
        else:
            result += alfa

    return result


print(to_alternating_case("hello world"))