# 문제 주소
# https://www.acmicpc.net/status?user_id=gks4478&problem_id=1157&from_mine=1

a = input()
a = a.upper()

cnt = []
cnt_2 = []
for i in set(a):
  cnt_2.append(i)
  cnt.append(a.count(i))

print('?') if cnt.count(max(cnt)) > 1 else print(cnt_2[cnt.index(max(cnt))])