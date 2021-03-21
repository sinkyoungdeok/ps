"""
문제 링크: https://www.acmicpc.net/problem/1431
문제 접근 방법: 정렬
"""

N = int(input())

serial_list = []
for i in range(N):
    serial = input()

    two_sum = 0
    for j in serial:
        if '0' <=j and j <= '9':
            two_sum += int(j)

    serial_list.append((serial, len(serial), two_sum))

serial_list.sort(key=lambda serial: (serial[1],serial[2],serial[0]))

for i in serial_list:
    print(i[0])