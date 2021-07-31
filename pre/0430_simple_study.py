# 최대 공약수 1
def find_gcd_1(a, b):
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return a

find_gcd_1(48, 60)

# 최대공약수 2
def find_gcd_2(a, b):
    while b!=0:
        temp=b
        b = a%b
        a = temp
    return a

find_gcd_2(48, 60)
find_gcd_2(48, 600)

# 옥스포드 문제
def count_open_door(n):
    doors = [-1]*n
    List = []
    for N in range(1, n+1):
        for i in range(N, n+1,N):
            doors[i-1]*=-1
    for j in range(n):
        if doors[j]==1:
            List.append(j+1)
    return List

count_open_door(1000)


# 콜라츠 추측
def is_loop(n):
    # 맨 처음에는 무조건 3을 곱하고 1을 더하기
    check = n*3+1
    # 1이 되거나, 돌아올 때 까지 반복시키기
    while check != 1:
        check = check//2 if check%2==0 else check*3+1
        if check==n:
            return True
    return False

count = 0
for i in range(2, 10000+1, 2):
    if is_loop(i):
        count+=1
print(count)

# 날짜의 2진수 변환1
# 연월일을 YYYYMMDD의 8자리 정수로 나타내었을 때 2진수로 변환하여
# 거꾸로 나열한 다음 다시 10진수로 되돌렸을 때 원래 날짜와 같은 날짜가 되는 것을
# 찾아보세요. 기간은 지난 도쿄 올림픽(19641010)부터 다음 도쿄올림픽(20200724)까지.

# 관련 모듈 불러오기
from datetime import datetime, timedelta
import time
S = time.time()

# 기간 설정
start = datetime.strptime('1964-10-10', '%Y-%m-%d')
end = datetime.strptime('2020-07-24', '%Y-%m-%d')
step = timedelta(days=1)

# 해당하는 날짜 찾아 출력하기
while start <= end:
    day = bin(int(start.strftime('%Y%m%d'))).replace('0b','')
    if day == day[::-1]:
        print(start.strftime('%Y%m%d'))
    start += step
E = time.time()
print(E-S)

# 날짜의 2진수 변환2

# 관련 모듈 불러오기
from datetime import datetime, timedelta
import time
S = time.time()

# 대상 기간에서 2진수의 5번째 문자부터 8개의 문자 추출
from_left = int(bin(19641010).replace('0b','')[4:4+8], 2)
to_left = int(bin(20200724).replace('0b','')[4:4+8], 2)

# 좌우의 8문자를 반복
for i in range(from_left, to_left+1):
    l = '{0:08b}'.format(i)
    r = l[::-1]
    for m in range(0, 1+1):
        value = '1001{}{}{}1001'.format(l, m, r)
        try:
            # 변환 가능한지 확인
            date = datetime.strptime(str(int(value, 2)), '%Y%m%d')
            # 변환 가능하면 출력
            print(date.strftime('%Y-%m-%d'))
        except:
            pass
E = time.time()
print(E-S)



##########
# 소수 찾기
##########

def find_Prime(n):
    nums = [False, False] + [True]*(n-1)
    for i in range(2, int(n**0.5)+1):
        if nums[i]:
            for j in range(2*i, n+1, i):
                nums[j] = False
    print(nums)
    return nums.count(True)

find_Prime(10)


def solution(n):
    check = [False, False] + [True]*(n-1)
    for i in range(2, int(n**0.5)+1):
        if check[i]:
            j=2
            while j*i <= n:
                check[i*j] =False
                j+=1
    print(check)
    return check.count(True)

solution(10)