# 문제 주소
# https://school.programmers.co.kr/learn/courses/30/lessons/120904
def solution(num, k):
    answer = 0
    if str(k) in str(num):
        answer = int(str(num).index(str(k))+1)
    else : 
        answer = -1
    return answer