# 문제 주소
# https://www.acmicpc.net/problem/1978
a = int(input())
b = list(map(int, input().split()))

c = 0
for i in b:
  cnt = 0
  for j in range(1, i+1):
    if i % j == 0:
      cnt += 1
  if cnt == 2:
    c += 1

print(c)