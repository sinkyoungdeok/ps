"""
문제 링크: https://www.acmicpc.net/problem/3613
문제 접근 방법: 구현
"""
s = input().rstrip()
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def java(txt):
    if txt[0] == "_" or txt[-1] == "_" or "__" in txt:
        return "Error!"
    ans = ""
    check = False
    for i in txt:
        if i in upper:
            return "Error!"
        
        if i == "_":
            check = True
            continue

        if check:
            ans += i.upper()
            check = False
            continue
        
        ans += i
    return ans

def cpp(txt):
    if txt[0] in upper:
        return "Error!"
    ans =""
    for i in txt:
        if i in upper:
            ans += "_" + i.lower()
        else:
            ans += i

    return ans

if "_" in s:
    print(java(s))
else:
    print(cpp(s))