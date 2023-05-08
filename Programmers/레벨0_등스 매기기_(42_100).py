# 문제 주소
# https://school.programmers.co.kr/learn/courses/30/lessons/120882
import numpy
def solution(score):
    cnt = 1
    answer = [''] * len(score)
    score = [numpy.mean(score[k]) for k in range(len(score))]
    while(cnt < len(score) + 1):
        index = [i for i,v in enumerate(score) if v == max(score)]
        for j in index : 
            answer[j] = cnt
            score[j] = -1
        cnt += len(index)
    return answer