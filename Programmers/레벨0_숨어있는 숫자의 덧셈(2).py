# https://school.programmers.co.kr/learn/courses/30/lessons/120864

def solution(my_string):
    for i in my_string:
        if i.isdigit() == False:
            my_string = my_string.replace(i,'-')
    my_string = list(map(int,filter(None,my_string.split('-'))))
    answer = sum(my_string)
    return answer