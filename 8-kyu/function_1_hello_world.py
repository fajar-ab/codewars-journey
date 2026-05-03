# Write a function `greet` that returns "hello world!"

# Rank  : 8 kyu
# Title : Function 1 - hello world
# Link  : https://www.codewars.com/kata/reviews/5485e5af4a0944ae2200016b/groups/69f6f0500ce9717116aa7733

def greet():
    with open(__file__) as f:
        line = f.readline()

    return line[-14:-2]
