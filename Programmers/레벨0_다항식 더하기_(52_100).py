# https://school.programmers.co.kr/learn/courses/30/lessons/120863

def solution(polynomial):
    value = 0
    value2 = 0
    answer = ''
    polynomial = polynomial.split()
    for i in filter(lambda x: polynomial[x] == '+', range(len(polynomial))) : polynomial[i] = 0
    
    for k in polynomial:
        if k != 0:
            if 'x' in k:
                if k[:-1] == '': value += 1
                else: value += int(k[:-1])
            else: value2 += int(k)
            
    if value != 0:
        if value != 1 and value2 != 0:
            answer = "%dx + %d" %(value, value2)
        elif value != 1 and value2 == 0:
            answer = "%dx" %(value)
        elif value == 1 and value2 != 0:
            answer = "x + %d" %(value2)
        elif value == 1 and value2 == 0:
            answer = 'x'
    else:
        if value2 == 0:answer = ''
        else : answer = str(value2)
        
    return answer