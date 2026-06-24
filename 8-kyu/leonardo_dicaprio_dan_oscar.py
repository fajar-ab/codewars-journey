# Rank  : 8 kyu
# Title : Leonardo Dicaprio dan Oscar
# Link  : https://www.codewars.com/kata/56d49587df52101de70011e4


def leo(oscar):
    return (
        "Leo finally won the oscar! Leo is happy"
        if oscar == 88
        else "Not even for Wolf of wallstreet?!"
        if oscar == 86
        else "When will you give Leo an Oscar?"
        if oscar < 88
        else "Leo got one already!"
    )
