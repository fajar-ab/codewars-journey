# Rank  : 8 kyu
# Title : Safen User Input Part I - htmlspecialchars
# Link  : https://www.codewars.com/kata/56bcaedfcf6b7f2125001118


def html_special_chars(data):
    return data.translate(
        str.maketrans({"<": "&lt;", ">": "&gt;", '"': "&quot;", "&": "&amp;"})
    )
