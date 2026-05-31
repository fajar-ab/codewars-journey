# Rank  : 8 kyu
# Title : Who ate the cookie?
# Link  : https://www.codewars.com/kata/55a996e0e8520afab9000055

def cookie(x):
    if type(x) is str:
        last_ate = "Zach"
    elif type(x) is float or type(x) is int:
        last_ate = "Monica"
    else:
        last_ate = "the dog"

    return f"Who ate the last cookie? It was {last_ate}!"
