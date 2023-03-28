# 문제 주소
# https://www.acmicpc.net/problem/2562
a_list = []
for i in range(9):
  a = int(input())
  a_list.append(a)
print(max(a_list))
print(a_list.index(max(a_list))+1)