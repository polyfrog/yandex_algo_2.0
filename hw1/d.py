# https://contest.yandex.ru/contest/28730/problems/D/

def school(students):
    return students[len(students) // 2]


n = int(input())
students = list(map(int, input().split()))
print(school(students))
