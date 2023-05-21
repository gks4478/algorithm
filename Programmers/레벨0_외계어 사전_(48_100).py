# 문제 주소
# https://school.programmers.co.kr/learn/courses/30/lessons/120869

def solution(spell, dic):
    result = 0
    for j in dic:
        for i in spell:
            if j.find(i) != -1:
                result += 1
        if result == len(spell):
            result = 1
            break
        else:
            result = 0

    if result != 1: result = 2

    return result