# https://contest.yandex.ru/contest/28738/problems/D/

def benches(l, k, blocks):
    middle = l // 2
    closest_l = blocks[0]
    for i in range(len(blocks)):
        if l % 2 == 1 and blocks[i] == middle:
            return [middle]
        elif blocks[i] < middle:
            closest_l = blocks[i]
        elif blocks[i] >= middle:
            return closest_l, blocks[i]


l, k = map(int, input().split())
blocks = list(map(int, input().split()))
print(*benches(l, k, blocks))
