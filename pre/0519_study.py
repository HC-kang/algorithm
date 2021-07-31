# 68제

import re
a = b = 1
count = 0
while count <11:
    c= a+b
    # 1자리씩 분할하여 자릿값 취득
    sum = 0
    for e in str(c):
        sum += int(e)
        if c% sum ==0:
            # 나누어 떨어지면 출력
            print(c)
            count +=1
            a, b = b, c

#################
from math import sqrt
# 정수 포함
i = 1
while True:
    i += 1
    # 소수점을 제거하고 왼쪽 10문자 추출
    string = '{:10.10f}'.format(sqrt(i)).replace('.','')[:10]
    # 중복을 제거해서 10문자라면 종료
    if len(set(string)) == 10:
        break

print(i)

# 소수만
i = 1
while True:
    i += 1
    # 소수점으로 분할하여 소수 부분만을 취득
    string = '{:10.10f}'.format(sqrt(i)).split('.')[1]
    # 소수부분의 중복을 제거하고 10문자라면 종료
    if len(set(string)) == 10:
        break

print(i)