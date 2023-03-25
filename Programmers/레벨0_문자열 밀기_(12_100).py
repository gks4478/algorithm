# 문제 주소
# https://school.programmers.co.kr/learn/courses/30/lessons/120921
def solution(A, B):
    A = list(A)
    B = list(B)
    C = ['']*len(A)
    answer = -1

    if A == B : answer = 0
    else:
        for cnt in range(1, len(A)):
            cnt2 = -(len(A) - cnt)
            for k in range(len(A)):
                try:
                    C[k+cnt] = A[k]
                except IndexError:
                    C[k+cnt2] = A[k]
            if C == B : 
                answer = cnt
                break

    return answer