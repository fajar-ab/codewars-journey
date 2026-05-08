# Rank  : 8 kyu
# Title : Find the stray number
# Link  : https://www.codewars.com/kata/57f609022f4d534f05000024

def stray(arr):
    """cara lebih aman adalah melihat berapa bayak angka yang muncul
    di dalam list dan bandingkan angka yang muncul hanya satu"""
    for value in arr:
        if arr.count(value) == 1:
            return value

print(stray([1, 1, 1, 1, 1, 1, 2]))

