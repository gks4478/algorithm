# 문제 주소
# https://www.acmicpc.net/problem/1924

# 제라 공식 이용
month,day= map(int, input().split())
date= ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
if month == 1:
    print(date[(21*20//4 + 5*6//4 + 26*(13+1)//10 + day - 1)%7])
elif month == 2:
    print(date[(21*20//4 + 5*6//4 + 26*(14+1)//10 + day - 1)%7])
else:
    print(date[(21*20//4 + 5*7//4 + 26*(month+1)//10 + day - 1)%7])

# 다른 코드
import sys
input= sys.stdin.readline
month,day= map(int, input().split())
days= [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
date= ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

sum= 0
for i in range(month - 1):
    sum += days[i]

sum += day

print(day[sum%7])