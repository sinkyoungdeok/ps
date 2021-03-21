"""
문제 링크: https://www.acmicpc.net/problem/1302
문제 접근 방법: 해시&정렬
"""

N = int(input())

book_dic = {}

for i in range(N):
    book = input()
    
    if book_dic.get(book):
        book_dic[book] += 1
    else:
        book_dic[book] = 1
    
book_list = list(book_dic.items())
book_list.sort(key=lambda book: (-book[1], book[0]))
print(book_list[0][0])
    
