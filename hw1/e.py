# https://contest.yandex.ru/contest/28730/problems/E/

from math import sqrt

def triangle(d, x0, y0):
    x1, y1, x2, y2, x3, y3 = 0, 0, d, 0, 0, d
    a = (x1 - x0) * (y2 - y1) - (x2 - x1) * (y1 - y0)
    b = (x2 - x0) * (y3 - y2) - (x3 - x2) * (y2 - y0)
    c = (x3 - x0) * (y1 - y3) - (x1 - x3) * (y3 - y0)
    if a >= 0 and b >= 0 and c >= 0:
        return 0
    dist = [sqrt((j[0] - x0) ** 2 + (j[1] - y0) ** 2) for j in [(x1, y1), (x2, y2), (x3, y3)]]
    return dist.index(min(dist)) + 1


d = int(input())
x0, y0 = list(map(int, input().split()))
print(triangle(d, x0, y0))
