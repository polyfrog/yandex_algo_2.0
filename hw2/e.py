# https://contest.yandex.ru/contest/28738/problems/E/

def diploma(arr):
    return sum(arr) - max(arr)


n = int(input())
arr = list(map(int, input().split()))
print(diploma(arr))
