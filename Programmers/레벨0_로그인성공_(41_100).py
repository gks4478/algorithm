# 문제 주소
# https://school.programmers.co.kr/learn/courses/30/lessons/120883

def solution(id_pw, db):
    answer = ''
    
    if id_pw in db : answer = "login"
    else : 
        for i in range(len(db)):
            if id_pw[0] == db[i][0] : 
                if id_pw[1] != db[i][1] : 
                    answer = "wrong pw"
                    break
            else : answer = "fail"
    return answer