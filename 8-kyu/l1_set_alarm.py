# Rank  : 8 kyu
# Title : L1: Set Alarm
# URL   : https://www.codewars.com/kata/reviews/5c2bd001b699cb00017ab489/groups/5c2c1b698c480e0001e88850

def set_alarm(employed, vacation):
    if employed and not vacation:
        return True
    return False
