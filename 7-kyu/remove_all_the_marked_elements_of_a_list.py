# Rank  : 7 kyu
# Title : Remove All The Marked Elements of a List
# Link  : https://www.codewars.com/kata/563089b9b7be03472d00002b


class List:
    def remove_(self, integer_list, values_list):    
        return [number for number in integer_list if number not in values_list]