# boj.kr/10991

n= int(input()) # 숫자를 입력받는다.
for i in range(1, n+1):
    print(('* '*i).center((n*2)-1).rstrip()) # 마지막 공백을 지워져야 출력형식이 맞음
# 새롭게 아게 된것: center(길이, '추가할 문자(생략O)')

# 마지막 공백 하나 정도는 봐준다.
n= int(input())
for i in range(1, n+1):
    print(' '*(n-i) + '* '*i)