# 문제 주소
# https://school.programmers.co.kr/learn/courses/30/lessons/120868

def solution(sides):
    sides_max = max(sides)
    sides_min = min(sides)
    answer = []
    for i in range(1,sides_max+1):
        if i + sides_min > sides_max : answer.append(i)
    for j in range(sides_max+1,sum(sides)):
        answer.append(j)
    return len(answer)