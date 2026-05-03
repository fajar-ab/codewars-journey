# Rank  : 7 kyu
# Title : List Filtering
# Link  : https://www.codewars.com/kata/reviews/53dbd54c3721866025000604/groups/61e453db9a04f80001a6c187

def filter_list(values):
    return [value for value in values if isinstance(value, int)]