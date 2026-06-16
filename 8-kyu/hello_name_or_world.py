# Rank  : 8 kyu
# Title : Hello, Name or World!
# Link  : https://www.codewars.com/kata/57e3f79c9cb119374600046b


def hello(name=""):
    return "Hello, {}!".format(name.title() or "World")
