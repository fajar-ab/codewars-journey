# Rank  : 7 kyu
# Title : Cat and Mouse Easy Version
# Link  : https://www.codewars.com/kata/57ee24e17b45eff6d6000164

def cat_mouse(x):
    return ["Caught!", "Escaped!"][x.count('.') > 3]
