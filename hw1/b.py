# https://contest.yandex.ru/contest/28730/problems/B/

def subway(i, j):
    i, j = min(i, j), max(i, j)
    return min((j - i - 1), (num - 1) - (j - i))


num, i, j = map(int, input().split())
print(subway(i, j))
