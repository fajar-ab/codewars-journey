# Rank  : 8 kyu
# Title : Triple Trouble
# Link  : https://www.codewars.com/kata/5704aea738428f4d30000914

def triple_trouble(one, two, three):
    return "".join(a + b + c for a, b, c in zip(one, two, three))
    
