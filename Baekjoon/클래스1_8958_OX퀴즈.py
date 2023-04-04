# 문제 주소
# https://www.acmicpc.net/problem/8958
a = int(input())
for i in range(a):
  b = input()
  c = 0
  cnt = 1
  for j in b:
    if j == 'O':
      c += cnt
      cnt += 1
    else:
      cnt = 1
  print(c)