# https://school.programmers.co.kr/learn/courses/30/lessons/120861

def solution(keyinput, board):
    board_max = [board[0]//2, board[1]//2]
    board_min = [-(board[0]//2), -(board[1]//2)]
    w = 0
    l = 0

    for k in keyinput:
        if k == "left" : 
            if  w == board_min[0] : w += 0
            else : w -= 1
        elif k == "right" :
            if w == board_max[0] : w += 0
            else : w += 1
        elif k == "down":
            if l == board_min[1] : l += 0
            else : l -= 1
        elif k == "up":
            if l == board_max[1] : l += 0
            else : l += 1
    answer = [w,l]
    return answer