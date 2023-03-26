# 문제 주소
# https://www.acmicpc.net/problem/10952
cnt = 0
while cnt == 0:
  A, B = map(int, input().split())
  if A == 0 & B == 0:
    cnt = -1
    break
  else:
    print(A+B)