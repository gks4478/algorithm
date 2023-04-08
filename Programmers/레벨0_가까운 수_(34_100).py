# 문제 주소
# https://school.programmers.co.kr/learn/courses/30/lessons/120890
def solution(array, n):
    value = list(map(lambda x: abs(n-abs(x)), array))
    value_min = min(value)
    value2 = list(filter(lambda x: value[x] == value_min, range(len(array))))
    value3 = list(map(lambda x: array[x], value2))
    answer = min(value3)
    return answer