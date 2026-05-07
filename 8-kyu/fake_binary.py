# Rank  : 8 kyu
# Title : Fake Binary
# Link  : http://codewars.com/kata/57eae65a4321032ce000002d

def fake_bin(x):
    """
    melakukan pemetaan karakter <=5 mendadi 0 dan >5 atau penggantian karakter 
    secara massal dengan efisiensi tinggi.
    """
    map = str.maketrans('0123456789', '0000011111')
    return x.translate(map)