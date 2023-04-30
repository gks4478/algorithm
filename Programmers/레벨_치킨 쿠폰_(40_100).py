# 문제 주소
# https://school.programmers.co.kr/learn/courses/30/lessons/120884

def solution(chicken):
    answer = 0
    while True:
        if chicken > 9:
            value1 = chicken // 10
            value2 = chicken % 10
            answer += value1
            chicken = value1 + value2
        else:
            break
    return answer