# 문제 주소
# https://www.acmicpc.net/problem/1259
while(True):
  a = input()
  if a == '0':
    break
  b = a[::-1]  
  if a == b:
    print('yes')
  else:
    print('no')