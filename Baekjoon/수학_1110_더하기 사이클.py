# 문제 주소
# https://www.acmicpc.net/problem/1110
a = input()
if len(a) == 2:
  v1 = a[0]
  v2 = a[-1]
else:  
  v1 = 0
  v2 = a[-1]
  a = '0' + a

cnt = 0
while(True):
  v3 = str(int(v1) + int(v2))[-1]
  cnt += 1
  if (v2 == a[0]) & (v3 == a[-1]):
    break
  else:
    v1 = v2[-1]
    v2 = v3[-1]

print(cnt)