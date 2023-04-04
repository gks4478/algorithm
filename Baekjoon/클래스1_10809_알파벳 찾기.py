# 문제 주소
# https://www.acmicpc.net/problem/10809
import string
c = string.ascii_lowercase
a = [-1]* 26
b = input()
for i in b:
  a[c.index(i)] = b.index(i)
print(' '.join(map(str, a)))