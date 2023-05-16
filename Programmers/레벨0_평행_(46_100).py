# 문제 주소
# https://school.programmers.co.kr/learn/courses/30/lessons/120875

def solution(dots):
    dots = sorted(dots)

    v1 = (dots[1][1] - dots[0][1]) / (dots[1][0] - dots[0][0])
    v2 = (dots[3][1] - dots[2][1]) / (dots[3][0] - dots[2][0])

    if v1 == v2 : answer = 1
    else : answer = 0
    
    return answer




