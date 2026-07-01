# Rank  : 8 kyu
# Title : Simple validation of a username with regex
# Link  : https://www.codewars.com/kata/56a3f08aa9a6cc9b75000023


def validate_usr(username):
    return 4 <= len(username) <= 16 and all(
        c.islower() or c.isdigit() or c == "_" for c in username
    )
