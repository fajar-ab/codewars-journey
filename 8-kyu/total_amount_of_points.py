# Rank  : 8 kyu
# Title : Total amount of points
# Link  : https://www.codewars.com/kata/reviews/5bb9109b16a8f195ea001643/groups/69fa176fdd8763af86f07064

def points(games):
    point = 0
    for points in games:
        x, y = points.split(":")
        point += 3 if x > y else 0 if x < y else 1

    return point

print(points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']))