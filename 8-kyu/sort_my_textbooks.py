# Rank  : 8 kyu
# Title : Sort My Textbooks
# Link  : https://www.codewars.com/kata/5a07e5b7ffe75fd049000051


def sorter(textbooks):
    return sorted(textbooks, key=lambda c: c.casefold())
