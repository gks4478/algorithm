# 문제 주소
# https://school.programmers.co.kr/learn/courses/30/lessons/120895


def solution(my_string, num1, num2):
    p = list(my_string)
    a = p[num1]
    b = p[num2]
    p[num1] = b
    p[num2] = a
    answer = ''.join(p)
    return answer