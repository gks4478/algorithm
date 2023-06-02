# 문제 주소
# https://www.acmicpc.net/problem/2441

value= int(input())
for i in range(value, 0, -1):
    print(' ' * (value-i) +  '*' * i)