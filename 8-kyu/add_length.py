# Rank  : 8 kyu
# Title : Add Length
# Link  : https://www.codewars.com/kata/559d2284b5bb6799e9000047


def add_length(str_):
    return [f"{word} {len(word)}" for word in str_.split()]


assert add_length("apple ban") == ["apple 5", "ban 3"]
assert add_length("you will win") == ["you 3", "will 4", "win 3"]
assert add_length("you") == ["you 3"]
assert add_length("y") == ["y 1"]
