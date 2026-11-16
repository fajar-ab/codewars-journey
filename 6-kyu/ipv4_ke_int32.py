# Rank  : 6 kyu
# Title : IPv4 ke int32
# Link  : https://www.codewars.com/kata/52ea928a1ef5cfec800003ee


def ip_to_int32(ip):
    bin32 = "".join(format(n, "08b") for n in map(int, ip.split(".")))
    return int(bin32, 2)
