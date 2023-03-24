# 문제 주소
# https://www.acmicpc.net/problem/2884
h,m = map(int, input().split())
v1 = ((h*60) + m - 45) // 60
v2 = ((h*60) + m - 45) % 60
if v1 < 0:
  v1 = 24 + v1
print(v1, v2)