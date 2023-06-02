# 문제 주소
# https://www.acmicpc.net/problem/2442

value= int(input())
for i in range(2*value-2, -1, -2):
    print(' '*(i//2) + '*'*(2*value-1-i))

# 다른 사람 풀이 : 정말 한끝 차이였다.
value= int(input())
for i in range(1, value+1):
    print(' '*(value-i) + '*'*(2*i-1))