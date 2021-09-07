# https://contest.yandex.ru/contest/28730/problems/C/

def date(x, y, z):
    return int((x > 12 or y > 12) or x == y)


x, y, z = map(int, input().split())
print(date(x, y, z))
