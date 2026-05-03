# Rank  : 7 kyu
# Title : List Filtering
# Link  : https://www.codewars.com/kata/53dbd5315a3c69eed20002dd

def filter_list(values):
    return [value for value in values if isinstance(value, int)]