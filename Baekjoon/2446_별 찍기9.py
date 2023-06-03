# 문제 주소
# https://www.acmicpc.net/problem/2446

value= int(value()) * 2
for i in range(value-1, 1, -2):
    print(' '*((value-i)//2) + '*'*(i))

for i in range(1, value, 2):
    print(' '*((value-i)//2) + '*'*(i))