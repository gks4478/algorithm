# 문제 주소
# https://www.acmicpc.net/problem/11022
cnt = int(input())
for i in range(cnt):
  a,b = map(int,input().split())
  print('Case #{0}: {1} + {2} = {3}'.format(i+1, a, b, a+b))