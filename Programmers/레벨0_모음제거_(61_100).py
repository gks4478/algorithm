import re
def solution(my_string):
    
    answer = re.sub(r"['a','e','i','o','u']","",my_string.lower())
    return answer