# 문제주소
# https://school.programmers.co.kr/learn/courses/30/lessons/120907
def solution(quiz):
    def o_x(value):
        if str(value) == q[-1]:
            answer[cnt] = "O"
        else:
            answer[cnt] = "X"
            
    answer = [''] * len(quiz)
    for i in range(len(quiz)) : quiz[i] = quiz[i].split()
    cnt = 0
    
    while(cnt < len(quiz)):
        for q in quiz:
            if q[1] == '-' :
                value = int(q[0]) - int(q[2])
                o_x(value)
            else:
                value = int(q[0]) + int(q[2])
                o_x(value)
            cnt += 1

    return answer
