# Rank  : 8 kyu
# Title : Calculate BMI
# Link  : https://www.codewars.com/kata/57a429e253ba3381850000fb

def bmi(weight, height):
    bmi = weight / height ** 2
    
    return {
        bmi > 30: "Obese",
        bmi <= 30.0: "Overweight",
        bmi <= 25.0: "Normal",
        bmi <= 18.5: "Underweight",
    }[True]
