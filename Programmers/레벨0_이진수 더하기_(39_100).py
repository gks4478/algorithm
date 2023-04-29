# 문제 주소
# https://school.programmers.co.kr/learn/courses/30/lessons/120885
def solution(bin1, bin2):
    answer = bin(int(bin1,2) + int(bin2,2))
    return answer[2:]