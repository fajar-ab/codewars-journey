# Rank  : 7 kyu
# Title : Remove anchor from URL
# Link  : https://www.codewars.com/kata/51f2b4448cadf20ed0000386

from urllib.parse import urldefrag

def remove_url_anchor(url):
    result = urldefrag(url)
    return result.url