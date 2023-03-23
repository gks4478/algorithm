# 문제 주소
# https://www.acmicpc.net/problem/2753

# (4의 배수 & !100의 배수) or (4의 배수 & 400의 배수)
year = int(input())
print(1) if ((year % 4 == 0) & (year % 100 != 0)) or ((year % 4 == 0) & (year % 400 == 0)) else print(0)