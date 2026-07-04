# Rank  : 6 kyu
# Title : Delete occurrences of an element if it occurs more than n times
# Link  : https://www.codewars.com/kata/554ca54ffa7d91b236000023


def delete_nth(order, max_e):
    temp = {}
    result = []

    for n in order:
        temp[n] = temp.get(n, 0) + 1

        if temp[n] <= max_e:
            result.append(n)

    return result


print(delete_nth([20, 37, 20, 21], 1), [20, 37, 21])
