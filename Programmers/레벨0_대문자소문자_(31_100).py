def solution(my_string):
    answer = []
    for i in my_string :
        if i.isupper() == True : answer.append(i.lower())
        else : answer.append(i.upper())
    answer = ''.join(answer)
    return answer