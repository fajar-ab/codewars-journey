# Rank  : 8 kyu
# Title : L1: Set Alarm
# Link  : https://www.codewars.com/kata/568dcc3c7f12767a62000038

def set_alarm(employed, vacation):
    if employed and not vacation:
        return True
    return False
