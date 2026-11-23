# Rank  : 7 kyu
# Title : Arithmetic progression
# Link  : https://www.cod/train/pythonewars.com/kata/55caf1fd8063ddfa8e000018


def arithmetic_sequence_elements(a, d, n):
    return ", ".join(str(a + i * d) for i in range(n))


print(arithmetic_sequence_elements(1, 2, 5))
