# 문제 주소
# https://www.acmicpc.net/problem/2609

a,b = map(int, input().split())
v1 = 1
for i in range(2, max(a,b)+1):
    while(a%i == 0 and b%i == 0):
        a = a // i
        b = b // i
        v1 *= i

print(v1)
print(v1*a*b)