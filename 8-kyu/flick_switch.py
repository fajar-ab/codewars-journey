# Rank  : 8 kyu
# Title : Flick Switch
# Link  : https://www.codewars.com/kata/64fbfe2618692c2018ebbddb


def flick_switch(lst):
    status = True
    return [(status := not status) if item == "flick" else status for item in lst]
