# 문제 주소
# https://www.acmicpc.net/problem/15552
import sys

T = int(input()) #Test case
for i in range(T):
  a,b = map(int, sys.stdin.readline().split())
  print(a+b)