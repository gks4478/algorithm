# 문제 주소
# https://www.acmicpc.net/problem/11050

import math

n,k= map(int, input().split())
print(int(math.factorial(n) / (math.factorial(k) * math.factorial(n-k))))