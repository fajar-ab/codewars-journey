# Rank  : 8 kyu
# Title : How old will I be in 2099?
# Link  : https://www.codewars.com/kata/5761a717780f8950ce001473


def calculate_age(year_of_birth, current_year):
    if (age := current_year - year_of_birth) == 1:
        return f"You are {age} year old."
    elif age == -1:
        return f"You will be born in {abs(age)} year."
    elif age > 0:
        return f"You are {age} years old."
    elif age < 0:
        return f"You will be born in {abs(age)} years."

    return "You were born this very year!"
