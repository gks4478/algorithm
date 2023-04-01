# 문제 주소
# https://school.programmers.co.kr/learn/courses/30/lessons/120909
import math
def solution(n):
    answer = 0
    value = math.sqrt(n) 
    if n % value == 0 : answer = 1
    else : answer = 2
    return answer
