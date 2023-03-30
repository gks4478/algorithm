# 문제 주소
# https://www.acmicpc.net/problem/2577

a = int(input())
b = int(input())
c = int(input())

cal = str(a*b*c)

for i in range(10):
  print(int(cal.count(str(i))))