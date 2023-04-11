# 문제 주소
# https://school.programmers.co.kr/learn/courses/30/lessons/120887

def solution(i, j, k):
    answer = 0
    value = ''
    
    for n in range(i,j+1):
        value += str(n)
    answer = value.count(str(k))
    return answer