# 문제 주소
# https://www.acmicpc.net/problem/2522

value= int(input())

for i in range(1, value):
    print(' '*(value-i) + '*'*i)
for i in range(value, 0, -1):
    print(' '*(value-i) + '*'*i)