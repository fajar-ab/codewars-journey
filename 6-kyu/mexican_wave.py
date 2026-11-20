# Rank  : 6 kyu
# Title : Mexican Wave
# Link  : http://codewars.com/kata/58f5c63f1e26ecda7e000029


def wave(people):
    return [
        people[:i] + people[i:].capitalize()
        for i in range(len(people))
        if people[i] != " "
    ]


print(wave("hello"))
