# 문제 주소
# https://www.acmicpc.net/problem/4153

import math
while(True):
    a = sorted(list(map(int, input().split())))
    if a[0] == 0 & a[1] == 0 & a[2] == 0:
        break
    else:
        if math.sqrt((a[0]**2) + (a[1]**2)) == a[2]:
            print('right')
        else:
            print('wrong')