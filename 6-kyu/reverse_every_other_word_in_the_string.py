# Rank  : 6 kyu
# Title : Reverse every other word in the string
# Link  : https://www.codewars.com/kata/58d76854024c72c3e20000de


def reverse_alternate(st):
    return " ".join(
        word if i % 2 == 0 else word[::-1] for i, word in enumerate(st.split())
    )


print(reverse_alternate(""))
print(reverse_alternate("Reverse this string, please!"))
