 # 문제 주소
# https://www.acmicpc.net/problem/10250

cnt = int(input())
for _ in range(cnt):
    a,b,c = map(int, input().split())
    room = []
    a *= 100
    d = 0
    for j in range(b):
        d += 1
        for i in range(100, a+100, 100):
            room.append(i+ d)
    print(room[c-1])