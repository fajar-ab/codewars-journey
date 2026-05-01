# Rank  : 6 kyu
# Title : Create Phone Number 
# Link  : https://www.codewars.com/kata/525f50e3b73515a6db000b83

def create_phone_number(number):
    str_number = "".join(map(str, number))
    return f"({str_number[:3]}) {str_number[3:6]}-{str_number[6:]}"