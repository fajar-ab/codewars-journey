# Rank  : 5 kyu
# Title : Calculating with Functions
# Link  : https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39


def make_number(n):
    def number(func=None):
        return n if func is None else func(n)

    return number


zero = make_number(0)
one = make_number(1)
two = make_number(2)
three = make_number(3)
four = make_number(4)
five = make_number(5)
six = make_number(6)
seven = make_number(7)
eight = make_number(8)
nine = make_number(9)


def plus(y):
    return lambda x: x + y


def minus(y):
    return lambda x: x - y


def times(y):
    return lambda x: x * y


def divided_by(y):
    return lambda x: x // y
