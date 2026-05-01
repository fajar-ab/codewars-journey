# Rank  : 6 kyu
# Title : Create Phone Number 
# URL   : https://www.codewars.com/kata/reviews/59b1a938182024506b00081d/groups/69f4811f27945203b1001114

def create_phone_number(number):
    str_number = "".join(map(str, number))
    return f"({str_number[:3]}) {str_number[3:6]}-{str_number[6:]}"