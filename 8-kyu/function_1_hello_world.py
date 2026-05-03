# Write a function `greet` that returns "hello world!"

# Rank  : 8 kyu
# Title : Function 1 - hello world
# Link  : https://www.codewars.com/kata/523b4ff7adca849afe000035

def greet():
    with open(__file__) as f:
        line = f.readline()

    return line[-14:-2]
