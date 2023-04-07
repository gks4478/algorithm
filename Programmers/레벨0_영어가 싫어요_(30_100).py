# 문제 주소
# https://school.programmers.co.kr/learn/courses/30/lessons/120894

def solution(numbers):
    numbers_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    index = -1
    
    for i in numbers_list:
        while True:
            index = numbers.find(i, index+1)
            if index != -1:
                numbers = numbers.replace(i,str(numbers_list.index(i)))
            else:
                break
    
    return int(numbers)
