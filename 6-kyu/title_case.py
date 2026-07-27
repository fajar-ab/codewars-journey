# Rank  : 6 kyu
# Title : Title Case
# Link  : https://www.codewars.com/kata/5202ef17a402dd033c000009


def title_case(title, minor_words=""):
    result = []

    for i, w in enumerate(title.lower().split()):
        if i != 0 and w in minor_words.lower().split():
            result.append(w.lower())
            continue

        result.append(w.title())

    return " ".join(result)


print(title_case(""))
