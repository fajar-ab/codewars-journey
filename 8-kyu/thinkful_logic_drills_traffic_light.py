# Rank  : 8 kyu
# Title : Thinkful - Logic Drills: Traffic light
# Link  : https://www.codewars.com/kata/58649884a1659ed6cb000072

def update_light(current):
    change = {"green":"yellow", "yellow":"red", "red":"green"}
    return change[current]
