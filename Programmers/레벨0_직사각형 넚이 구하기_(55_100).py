# https://school.programmers.co.kr/learn/courses/30/lessons/120860

def solution(dots):
    x_big = 0
    x_small = 0
    y_big = 0
    y_small = 0
    for i in range(1,len(dots))	:
        if dots[0][0] != dots[i][0] : 
            if dots[0][0] > dots[i][0] :
                x_big = dots[0][0]
                x_small = dots[i][0]
                break
            else:
                x_big = dots[i][0]
                x_small = dots[0][0]
                break

    for j in range(1,len(dots))	:
        if dots[0][1] != dots[j][1] : 
            if dots[0][1] > dots[j][1] :
                y_big = dots[0][1]
                y_small = dots[j][1]
                break
            else:
                y_big = dots[j][1]
                y_small = dots[0][1]
                break

    w = x_big - x_small
    h = y_big - y_small
    answer = w*h
    return answer