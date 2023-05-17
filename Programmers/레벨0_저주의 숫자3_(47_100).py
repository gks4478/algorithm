# 문제 주소
# https://school.programmers.co.kr/learn/courses/30/lessons/120871

def solution(n):
    answer = []
    cnt = 0
    while(len(answer) < n):
        cnt += 1
        if cnt%3 != 0 and "3" not in filter(int,str(cnt)):
            answer.append(cnt)
    return answer[-1]