# Rank  : 7 kyu
# Title : Jaden Casing Strings
# Link  : https://www.codewars.com/kata/5390bac347d09b7da40006f6

from string import capwords as to_jaden_case

"""
masalah dengan str.title() adalah menganggap setip karakter non-huruf 
sebagai pemisah kata sehingga jika kalimat yang akan dibuah

`How can mirrors be real if our eyes aren't real`

`aren't` akan menjasi `Aren'T` bukan menjadi `Aren't`

Modul bawaan string memiliki fungsi capwords yang lebih cerdas. 
Fungsi ini memecah kalimat berdasarkan spasi saja, sehingga 
tanda baca di dalam kata tidak akan memicu kapitalisasi.
"""