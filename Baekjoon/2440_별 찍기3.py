# 문제 주소
# https://www.acmicpc.net/problem/2440

value= int(input())
for i in range(value, 0, -1):
    print('*' * i)

# 다른 사람 코드 
for i in range(int(input()), 0, -1):print('*' * i)