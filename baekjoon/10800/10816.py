"""
문제 링크: https://www.acmicpc.net/problem/10816
문제 접근 방법: 해시
"""

N = int(input())
n_list = list(map(int,input().split()))
M = int(input())
m_list = list(map(int,input().split()))

dic = {}

for i in n_list:
    if dic.get(i):
        dic[i]+=1
    else:
        dic[i] =1

for i in m_list:
    if dic.get(i):
        print(dic[i], end=" ")
    else:
        print(0, end=" ")