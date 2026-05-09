# Rank  : 8 kyu
# Title : Transportation on vacation
# Link  : https://www.codewars.com/kata/568d0dd208ee69389d000016

def rental_car_cost(day):
    if day >= 7:
        total_costs = day * 40 - 50
    elif day >= 3:
        total_costs = day * 40 - 20
    else:
        total_costs = day * 40
    
    return total_costs