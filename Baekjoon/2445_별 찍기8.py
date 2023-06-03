# 문제 주소
# https://www.acmicpc.net/problem/2445

value= int(input())

for i in range(1, value+1):
    print('*'*i + ' '*(value*2-i*2) + '*'*i)
for i in range(value-1, 0, -1):
    print('*'*i + ' '*(value*2-i*2) + '*'*i)