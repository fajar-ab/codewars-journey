# Rank  : 7 kyu
# Title : Get the Middle Character
# Link  : https://www.codewars.com/kata/56747fd5cb988479af000028

def get_middle(s):
    """ divmod = (num // 2, num % 2) """
    index, odd = divmod(len(s), 2)
    return s[index] if odd else s[index-1: index+1]

print(get_middle("testing"))
