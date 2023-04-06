# 문제 주소
# https://school.programmers.co.kr/learn/courses/30/lessons/120896

def solution(s):
    return ''.join(sorted(list(filter(lambda x:s.count(x)==1,s))))