# Rank  : 7 kyu
# Title : Get the Middle Character
# Link  : https://www.codewars.com/kata/56747fd5cb988479af000028

def get_middle(s):
    mid = len(s) // 2
    if len(s) % 2 == 0:
        return s[mid-1:mid+1]
    return s[mid]

print(get_middle("testing"))
