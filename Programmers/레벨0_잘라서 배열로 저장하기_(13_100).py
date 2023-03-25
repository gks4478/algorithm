# 문제 주소
# https://school.programmers.co.kr/learn/courses/30/lessons/120913
import math
def solution(my_str, n):
    my_str_len = len(my_str)
    turn = math.ceil(my_str_len/n)
    answer = list(map(lambda i :my_str[(n*i)-n:(n*i)], range(1,turn+1)))
    return answer