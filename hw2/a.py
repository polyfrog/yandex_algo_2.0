# https://contest.yandex.ru/contest/28738/problems/A/

def equal_max(n):
    c = 1
    max = n
    while n != 0:
        n = int(input())
        if n == max:
            c += 1
        elif n > max:
            max = n
            c = 1
    return c

  
n = int(input())
print(equal_max(n))
