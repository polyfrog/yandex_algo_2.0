# https://contest.yandex.ru/contest/28738/problems/C/

def palindrome(string):
    if len(string) == 1:
        return 0
    if len(string) % 2 == 0:
        string = string[:len(string) // 2] + 'a' + string[len(string) // 2:]
    l, r = len(string) // 2 - 1, len(string) // 2 + 1
    price = 0
    for i in range(len(string) // 2):
        if string[l] != string[r]:
            price += 1
        l -= 1
        r += 1
    return price


string = input()
print(palindrome(string))
