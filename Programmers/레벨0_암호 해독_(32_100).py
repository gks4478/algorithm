# 문제 주소
# https://school.programmers.co.kr/learn/courses/30/lessons/120892
def solution(cipher, code):
    answer = cipher[code-1::code]
    return answer