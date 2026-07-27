# Rank  : 8 kyu
# Title : Localize The Barycenter of a Triangle
# Link  : https://www.codewars.com/kata/5601c5f6ba804403c7000004


def bar_triang(point_a, point_b, point_c):
    x, y = zip(*[point_a, point_b, point_c])
    return [round(sum(x) / 3, 4), round(sum(y) / 3, 4)]


print(bar_triang([4, 8], [8, 2], [16, 6]))
