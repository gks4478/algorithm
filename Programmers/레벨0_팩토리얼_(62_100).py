def solution(n):
    answer = 0
    fac = 1
    for i in range(1,12):
        fac *= i
        if fac > n:
            answer = i-1
            break
    return answer