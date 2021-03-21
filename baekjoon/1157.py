"""
문제 링크: https://www.acmicpc.net/problem/1157
문제 접근 방법: 단순 구현
"""
alphabet_count = []
word = input().upper()

for ascii_code in range(65, 91):
    alphabet_count.append(word.count(chr(ascii_code)))

max_count = max(alphabet_count)

if alphabet_count.count(max_count) > 1:
    print('?')
else:
    print(chr(alphabet_count.index(max_count)+65))