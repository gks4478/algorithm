# 문제 주소
# https://school.programmers.co.kr/learn/courses/30/lessons/120889
1
def solution(sides):
    answer = 0
    sides.sort()
    sides_max = sides[-1]
    
    if sides_max < sides[0] + sides[1] : answer = 1
    else : answer = 2
    
    return answer