# Rank  : 8 kyu
# Title : Number of People in the Bus
# Link  : https://www.codewars.com/kata/5648b12ce68d9daa6b000099

def number(bus_stops):
    still_on_the_bus  = 0
    for get_on, get_off in bus_stops:
        still_on_the_bus += get_on - get_off

    return still_on_the_bus