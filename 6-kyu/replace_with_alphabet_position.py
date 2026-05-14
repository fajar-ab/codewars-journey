# Rank  : 6 kyu
# Title : Replace With Alphabet Position
# Link  : https://www.codewars.com/kata/546f922b54af40e1e90001da

new_ord = lambda c: str(ord(c) - ord("a") + 1)
def alphabet_position(text): 
    return " ".join(list(map(new_ord, filter(str.isalpha, text.lower()))))

print(alphabet_position("The sunset sets at twelve o' clock."))