# 문제 주소
# https://www.acmicpc.net/problem/8393

value= int(input())
sum= value
for i in range(1, value):
    sum += i
print(sum)

# 다른 사람 풀이 왜 이런 생각이 안 드는 걸까?
n= int(input())
print(n*(n+1)//2)