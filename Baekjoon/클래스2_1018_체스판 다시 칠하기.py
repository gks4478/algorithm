# 문제 주소
# https://www.acmicpc.net/problem/1018

# 행 열 입력
a, b = map(int, input().split())

# 문자열 입력
value = [input() for _ in range(a)]

# 행
c = b - 8
d = list(range(c+1))
e = list(range(7, b))

# 열
h = a - 8
f = list(range(7, a))
g = list(range(h + 1))

# 배열 2가지
type1 = 'WBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBW'
type2 = 'BWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWB'

# 저장할 리스트 2개
t1 = []
t2 = []

# 반복
for k in range(h + 1):
  for j in range(c + 1):
    stack = ''
    for i in range(g[k], f[k]+1):
      stack += value[i][d[j]:e[j]+1]
    t1.append(str(sum(s1 != s2 for s1, s2 in zip(stack, type1))))
    t2.append(str(sum(s1 != s2 for s1, s2 in zip(stack, type2))))

# t1, t2 합쳐서 가장 작은값 출력하기 
print(min(list(map(int, t1+t2))))