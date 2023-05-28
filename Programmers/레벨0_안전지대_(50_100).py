# 문제 주소
# https://school.programmers.co.kr/learn/courses/30/lessons/120866
def solution(board):
    result = [[0 for a in range(len(board) + 2)] for b in range(len(board) + 2)]
    
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                result[i + 1][j + 1] = 1
                result[i + 1][j] = -1
                result[i + 1][j + 2] = -1
                result[i + 2][j] = -1
                result[i + 2][j + 1] = -1
                result[i + 2][j + 2] = -1
                result[i][j] = -1
                result[i][j + 1] = -1
                result[i][j + 2] = -1

    answer = 0
    for m in range(1, len(board) + 1):
        for n in range(1, len(board) + 1):
            if result[m][n] == 0:
                answer += 1

    return answer