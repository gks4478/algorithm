# https://school.programmers.co.kr/learn/courses/30/lessons/120862

def solution(numbers):
    answer = 0
    numbers.sort()
    answer = max(numbers[0]*numbers[1], numbers[-1]*numbers[-2])
    return answer