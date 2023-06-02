# 문제 주소
# https://www.acmicpc.net/problem/11718

# 문자열이 입력되지 않으면 무한 반복문을 나간다.
while(True):
    try:
        print(input())
    except:
        break