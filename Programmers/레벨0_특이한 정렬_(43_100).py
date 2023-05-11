# 문제주소
# https://school.programmers.co.kr/learn/courses/30/lessons/120880

def solution(numlist, n):
    answer = []
    value = []

    for i in numlist:
        save = n - i
        if save < 0:
            save = abs(n-i) - 0.1
        value.append(save)

    for j in numlist:
        index = value.index(min(value))
        answer.append(numlist[index])
        value[index] = 10001
        
    return answer