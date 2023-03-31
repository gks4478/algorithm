# 문제 주소
# https://www.acmicpc.net/problem/1085
x, y, w, h = list(map(int, input().split()))
print(min([abs(x-w), abs(y-h), x,y]))