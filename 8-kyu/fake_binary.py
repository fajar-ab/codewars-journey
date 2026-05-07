# Rank  : 8 kyu
# Title : Fake Binary
# Link  : http://codewars.com/kata/57eae65a4321032ce000002d

def fake_bin(x):
    return "".join(['0' if int(a) < 5 else '1' for a in x])

def fake_bin(x):
    return "".join([str(int(a >= 5)) for a in map(int, x)])

def fake_bin(x):
    return "".join([str(int(a // 5)) for a in map(int, x)])
