# Rank  : 6 kyu
# Title : Help the bookseller !
# Link  : https://www.codewars.com/kata/54dc6f5a224c26032800005c


def stock_list(stocklist, categories):
    categories = dict.fromkeys(categories, 0)

    if not stocklist:
        return ""

    for item in stocklist:
        b, c = item.split()
        if (label := b[0]) in categories:
            categories[label] = categories.get(label, 0) + int(c)

    return " - ".join(f"({l} : {c})" for l, c in categories.items())


print(
    stock_list(
        ["HRAPO 923", "HCKGT 844"],
        ["W", "V"],
    )
)
