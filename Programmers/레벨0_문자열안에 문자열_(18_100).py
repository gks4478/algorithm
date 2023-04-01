# 문제 주소
# https://school.programmers.co.kr/learn/courses/30/lessons/120908
def solution(str1, str2):
    answer = 0
    value = str1.find(str2)
    if value == -1 : answer = 2
    else : answer = 1
    return answer