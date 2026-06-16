# Rank  : 6 kyu
# Title : Who likes it?
# Link  : https://www.codewars.com/kata/5266876b8f4bf2da9b000362


def likes(names):
    return (
        "no one likes this"
        if not names
        else "{} likes this".format(*names)
        if len(names) == 1
        else "{} and {} like this".format(*names)
        if len(names) == 2
        else "{}, {} and {} like this".format(*names)
        if len(names) == 3
        else "{}, {} and {} others like this".format(*names[:2], len(names[2:]))
    )


print(likes(["Alex", "Jacob", "Mark", "Max"]))
