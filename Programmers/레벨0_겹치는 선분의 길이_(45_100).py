# 문제 주소
# https://school.programmers.co.kr/learn/courses/30/lessons/120876

def solution(lines):
    lines = sorted([[i for i in range(lines[k][0],lines[k][1])] for k in range(3)], key = lambda x : len(x))
    if (len(lines[0])+len(lines[1])) < len(lines[2]) or (len(lines[0])+len(lines[1])) == len(lines[2]):
        v1 = set(lines[0]) & set(lines[2])
        v2 = set(lines[1]) & set(lines[2])
    else:
        lines = sorted(lines)
        v1 = set(lines[0]) & set(lines[1])
        v2 = set(lines[2]) & set(lines[1])
    answer = len(v1) + len(v2) - len(v1&v2)
    return answer