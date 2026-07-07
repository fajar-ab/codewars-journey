# Rank  : 7 kyu
# Title : V A P O R C O D E
# Link  : https://www.codewars.com/kata/5966eeb31b229e44eb00007a


def vaporcode(s):
    return "  ".join(c.upper() for c in s if not c.isspace())
