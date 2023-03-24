# 문제 주소
# https://school.programmers.co.kr/learn/courses/30/lessons/120923
def solution(num, total):
    if num % 2 == 0 : answer = [''] * (num + 1)
    else : answer = [''] * num

    answer[num//2] = total//num

    for m in range((num//2)-1, -1, -1) : answer[m] = answer[m+1] -1
    for n in range((num//2)+1, len(answer)) : answer[n] = answer[n-1] + 1

    if len(answer) != num : del answer[0]
    
    return answer