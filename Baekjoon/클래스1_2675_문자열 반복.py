# 문제 주소
# https://www.acmicpc.net/problem/2675
cnt = int(input())
for i in range(cnt):
  v = input().split()
  print(''.join([i*int(v[0]) for i in v[1]]))