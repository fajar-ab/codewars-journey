# Rank  : 8 kyu
# Title : Exclamation marks series #11: Replace all vowel to exclamation mark in the sentence
# Link  : https://www.codewars.com/kata/57fb09ef2b5314a8a90001ed

def replace_exclamation(st):
    return st.translate(str.maketrans("aiueoAIUEO", '!!!!!!!!!!'))
