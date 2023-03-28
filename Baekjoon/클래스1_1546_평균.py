# 문제 주소
# https://www.acmicpc.net/problem/1546
cnt = int(input())
a = list(map(int, input().split()))

total = 0
for i in range(cnt):
  m = max(a)
  total += a[i]/m * 100

print(total/cnt)