# https://school.programmers.co.kr/learn/courses/30/lessons/120853

def solution(s):
    answer = 0
    s = s.split()
    for i in range(len(s)):
        if s[i] == 'Z' : s[i] = -(int(s[i-1]))

    for j in s:
        answer += int(j)
        
    return answer