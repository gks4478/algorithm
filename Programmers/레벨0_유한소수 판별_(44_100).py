# 문제 주소
# https://school.programmers.co.kr/learn/courses/30/lessons/120878
def solution(a, b):
    
    answer = 2
    
    if b == 1 : answer = 1
    else:
        for k in range(2, max(a,b)+1):
            if a%k == 0 and b%k == 0:
                a = a//k
                b = b//k
        
        for i in range(2, 6, 3):
            while(b%i == 0):
                b = b//i
            if b == 1 : answer = 1
            
    return answer