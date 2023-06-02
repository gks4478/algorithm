# 문제 주소
# https://www.acmicpc.net/problem/11721

# 쉬운걸 엄청 어렵게 풀었네;;
import math
a= input()

if len(a)<11:
    print(a[:len(a)+1])
else:
    for i in range(1, math.ceil(len(a)/10)+1):
        print(a[i*10-10:i*10])

# 간단한 코드
a= input()
for i in range(0, len(a), 10):
    print(a[i:i+10])