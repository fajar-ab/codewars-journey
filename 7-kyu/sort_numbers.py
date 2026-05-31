# Rank  : 7 kyu
# Title : Sort Numbers
# Link  : https://www.codewars.com/kata/5174a4c0f2769dd8b1000003

# menggunakan nilai operand
solution = lambda nums: sorted(nums or [])

print(solution(None))
print(solution([1,2,3,10,5]))
