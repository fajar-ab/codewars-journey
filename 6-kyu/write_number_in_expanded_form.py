# Rank  : 6 kyu
# Title : Write Number in Expanded Form
# Link  : https://www.codewars.com/kata/5842df8ccbd22792a4000245


def expanded_form(num):
    return " + ".join(
        reversed([c + ("0" * i) for i, c in enumerate(str(num)[::-1]) if c != "0"])
    )


print(expanded_form(12))
print(expanded_form(42))
print(expanded_form(70304))
