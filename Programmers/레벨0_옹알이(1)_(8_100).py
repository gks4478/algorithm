# 문제 주소
# https://school.programmers.co.kr/learn/courses/30/lessons/120956
def solution(babbling):
    can = ["aya", "ye", "woo", "ma"]
    for i in range(len(babbling)):
        for j in can:
            if j in babbling[i]:
                babbling[i] = babbling[i].replace(j, '.')

    for k in range(len(babbling)):
        babbling[k] = babbling[k].replace('.','')

    answer = babbling.count('')
    return answer