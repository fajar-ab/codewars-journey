# Rank  : 8 kyu
# Title : Convert boolean values to strings 'Yes' or 'No'
# Link  : https://www.codewars.com/kata/53369039d7ab3ac506000467

def bool_to_word(boolean):
    """dapat menggunakan nilai bolean untuk mengakses index di dalam list
    namun cara ini hanya bisa jika length dari list sama dengan 2"""
    return ["No", "Yes"][boolean]

print(bool_to_word(True))
print(bool_to_word(False))