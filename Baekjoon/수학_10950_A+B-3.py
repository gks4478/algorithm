# 문제 주소
# https://www.acmicpc.net/problem/10950
# 첫번째 있는 숫자 한개는 앞으로 몇개의 a,b를 입력할것이다라고 하는것
# 그래서 for문이 필요한것

value = int(input())
for i in range(value):
  a,b = input().split()
  print(int(a) + int(b))