"""
문제 링크: https://www.acmicpc.net/problem/1252
문제 접근 방법: 2진법으로 받은 값을 10진수로 변환하여 더해주고 다시 2진법으로 변경
"""

input_list = [ int(i,2) for i in input().split(" ")]
print(bin(sum(input_list))[2:])