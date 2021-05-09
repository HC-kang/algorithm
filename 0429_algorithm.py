# # 알고리즘 퍼즐 68 기초편

# # 1번

# # num = 123
# # print(num, type(num))
# # print(oct(num), type(oct(num)))
# # print(bin(num), type(bin(num)))

# # while True:
# #     num_10 = str(num)
# #     num_8 = oct(num).replace("0o", "")
# #     num_2 = bin(num).replace("0b", "")

# #     if num_10 == num_10[::-1]\
# #         and num_8 == num_8[::-1]\
# #         and num_2 == num_2[::-1]:
# #             print("answer : ", num)
# #             print(num_8)
# #             print(num_2)
# #             break
# #     else:
# #         num+=2


# # 2번

# # import re

# # op = ["*", ""]
# # for i in range(1000, 10000):
# #     c = str(i)
# #     for j in range(0, len(op)):
# #         for k in range(0, len(op)):
# #             for l in range(0, len(op)):
# #                 val = c[3] + op[j] + c[2] + op[k] + c[1] + op[1] + c[0]

# #                 # 0으로 시작하는 숫자가 있는지 확인하고
# #                 # 있는 경우 제거
# #                 val = re.sub(r"0(\d+)", r"\1", val)

# #                 if len(val) > 4:
# #                     if i == eval(val):
# #                         print(val, "=", i)

# ##################################

# # cards = [0]*100
# # print(cards)
# # for i in range(2, 100+1):
# #     for j in range(i, )

# #################################

# # 설탕

# # n = int(input())
# # f = n//5
# # t=0
# # if n==4 or n==7:
# #     print(-1)
# # elif n%5 ==1:
# #     f-=1
# #     t+=2
# #     print(f+t)
# # elif n%5 ==2:
# #     f-=2
# #     t+=4
# #     print(f+t)
# # elif n%5 ==3:
# #     t+=1
# #     print(f+t)
# # elif n%5 ==4:
# #     f-=1
# #     t+=3
# #     print(f+t)
# # else:
# #     print(f+t)

# ######################################

# # 전자레인지
# T = int(input())

# if T %10 !=0:
#     print(-1)
# else:
#     a = T // 300
#     b = T % 300 // 60
#     c = int(T % 300 % 60 / 10)
#     print(a, b, c)

# ######################################

# # 크게 만들기 2812

# # N 자리 숫자에서 K개 지워서 만들어지는 가장 큰 수 출력

# # N K
# # nnnn

# # N, K = input().split(' ')
# # number = input()
# # num_list = list(number)
# # print(num_list)
# # checklist=[]
# # for k in K:
# #     for n in N:
# #         removedlist = num_list.remove(n)
# #         print(removedlist)
# #         checklist.append(removedlist)
# #         print(checklist)
# # print(max(removedlist))

# # for i in range(N)

# # number[0, 1, 2, 3 . . . . N]

# # Max_num = 0




# # list_a = list('1234')
# # a =""
# # for i in list_a:
# #     a = a + i
# # print(a)

# ######################################
# # 수열의 사칙연산
# # 1,000 ~ 9,999 중에서 사이에 연산자를 넣어서 결과가 원래의 수를 거꾸로 한 수가 나오는 경우
# # ex1) 351 -> 3 * 51 = 153
# # ex2) 621 -> 6 * 21 = 126
# # ex3) 886 -> 8 * 86 = 588

# # # 곱셈 외 덧셈, 뺄셈, 나눗셈은 불가능

# # import re

# # op = ["*", ""] # 연산자 종류들 중 가능한 건 곱셈뿐 - 다른건 너무 작아짐.
# # for i in range(1000, 10000): # 범위지정
# #     c = str(i) # 우리가 찾는 숫자들을 하나식 대입

# #     # 각 숫자 사이에 연산자가 들어갈수 있게 for문 구성
# #     for j in range(0, len(op)):
# #         for k in range(0, len(op)):
# #             for l in range(0, len(op)):  
# #                 val = c[3] + op[j] + c[2] + op[k] + c[1] + op[l]+c[0]

# #                 # 0으로 시작하는 숫자가 있는지 확인하고
# #                 # 있는 경우 제거
# #                 val = re.sub(r"0(\d+)", r"\1", val)

# #                 # 연산자를 하나는 넣는 경우
# #                 if len(val) >4:
# #                     if i == eval(val):
# #                         print(val, "=", i)
# # #########
# # # 변형 (3자릿수)

# # import re

# # op = ["*", ""]
# # for i in range(100, 1000):
# #     c = str(i)
# #     for j in range(0, len(op)):
# #         for k in range(0, len(op)):
# #             val = c[2] + op[j] + c[1] + op[k] + c[0]

# #             # 0으로 시작하는 숫자가 있는지 확인하고
# #             # 있는 경우 제거
# #             val = re.sub(r"0(\d+)", r"\1", val)

# #             # 연산자를 하나는 넣는 경우
# #             if len(val) >3:
# #                 if i == eval(val):
# #                     print(val, "=", i)
# # #########
# # # 카드 뒤집기

# # # 카드 초기화
# # N = 100
# # cards = [False] * N # 카드 개수 설정 및 전체 뒷면으로 표시
# #         # 카드 인덱스 번호는 0~99

# # # 2 ~ N 까지 뒤집음
# # for i in range(2, N+1): # 2~100까지?
# #     j = i-1 # j 는 1부터 시작해서 99까지 갈 예정.
# #     while j < len(cards): # 최초 시작 j(=1, 카드번호 2)로 부터 i(=2, 최초)씩 증가하면서 뒤집기.
# #                           # 다음에는 j=2, 카드번호는 3, i는 3이므로 j는 2(카드번호3) 부터 3씩 증가
# #         cards[j] = not cards[j]
# #         j += i

# # # 뒷면이 위를 향한 카드 출력
# # for i in range(0, N):
# #     if not cards[i]:
# #         print(i+1)

# # #############
# # # 카드뒤집기 2

# # for i in range(1, 100+1):
# #     flag = False
# #     for j in range(1, 100+1):
# #         if i%j ==0:
# #             flag = not flag
# #     if flag:
# #         print(i)

# s = "Zbcdefg"	
# def solution(s):
#     words = []
#     answer = ''
    
#     for i in s: 
#         words.append(ord(i))
#     words = list(reversed(sorted(words)))
    
#     for j in words:
#         answer += chr(j)
#     return answer

# solution("ABCabc")

# ord('sd')

######

# 리스트 내의 사람들을 2명씩 짝짓는 모든 경우의 수를 출력

# list_a = ['강희', '정종', '김미', '서연', '현경']
# n = len(list_a)
# for i in range(0, n-1):
#     for j in range(i+1, n):
#         print('{0} - {1}'.format(list_a[i], list_a[j]))

# #####
# # 팩토리얼
# import time


# dictionary = {
#     1: 1,
#     2: 1
# }
# def fibo(n):
#     start = time.time()
#     if n in dictionary:
#         answer = dictionary[n]
#     else:
#         answer = fibo(n-1) + fibo(n-2)
#         dictionary[n] = answer
#     end = time.time()
#     print(end-start)
#     return answer

# fibo(100)

# #####
# #

# numlist = [1,2,3,4]
# numlist.remove(5)
# numlist

# n = 100
# def solution(n):
#     if n==2:
#         return False
#     for i in range(2, n):
#         if n%i ==0:
#             return False
#     return True


# for i in range(n+1):
#     if(solution(i)):
#         print(i)

# solution(10)


# def solution(n):
#     numlist = list(range(3, n+1, 2))
#     print(numlist)
#     result = [2]
#     print(result)

#     for i in range(n):
#         if i in numlist:
#             result.append(i)
        

#     return result

# solution(10)

# def solution(n):
#     check = [True]*(n+1)
#     check[0] = False
#     check[1] = False
#     for i in range(2, int(n**0.5)+1):
#         if check[i] == True:
#             j=2
#             while j*i <= n:
#                 check[i*j] =False
#                 j+=1
#     print(check)

#     return check.count(True)

# solution(10)

# #############

# def solution(n):
#     num=set(range(2,n+1))

#     for i in range(2,n+1):
#         if i in num:
#             num-=set(range(2*i,n+1,i))
#     return len(num)

# solution(10)


# def solution(n):
#     num = set(range(2, n+1))

#     for i in range(2, n+1):
#         if i in num:
#             num-=set(range(2*i, n+1, i))
#     return len(num)

# solution(10)

# def solution(absolutes, signs):
#     sum_list = []
#     signs = map(lambda x: if x==True : 1, elif x==False: -1, signs)
#     answer = 
    
#     return 
    
# signs = [True, False]
# signs = signs.replace(True, 1)

# def solution(absolutes, signs):
#     sum_ = 0
#     for i in range(len(signs)):
#         if signs[i]
#             sum_ += absolutes[i]
#         else:
#             sum_ -= absolutes[i]
#     return sum_

# solution([4, 7, 12], ['true', 'false', 'true'])


#####

def is_loop(n):
    num = n*3 + 1
    while num != 1:
        num = num//2 if num%2==0 else num*3+1
        if num==n:
            return True
    return False
import time
count = 0
start = time.time()
for i in range(2, 1000000+1, 2):
    if is_loop(i):
        count+=1
end = time.time()
print(count)
print(end-start)

###########3
# 소인수분해
p=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
m = int(input('수 입력 : '))
print(m, end = '=')

i=0
while(m!=1):
    while(m%p[i]==0):
        print(p[i], end='x')
        m=m/p[i]
    i += 1

#############
# 최대공약수 구하기 1

a = int(input('첫번째 수 입력 : '))
b = int(input('두번째 수 입력 : '))

while a!=b:
    if a>b:
        a = a-b
    else:
        b = b-a
print(a)

###############
# 최대공약수 구하기 2

a = int(input('첫번째 수 : '))
b = int(input('두번째 수 : '))

while b!=0:
    temp = b
    b = a%b
    a = temp
print(a)

48 60
a48
b60
t60
b48
a48

A = BQ+R

R = A%B, 즉 A%B==0일때까지.

42 = 8 5  +2

8 = 2 4 +0

##########
# 옥스포드 문제 = 카드뒤집기
# -1 : 닫힘
cards = [-1] * 100

for N in range(1, 100+1):
    for i in range(N, 100+1,N):
        cards[i-1] *= -1
print(cards.count(1))

open_list=[]
for i in range(len(cards)):
    if cards[i]==1:
        open_list.append(i+1)

###############
# 옥스포드 문제 다른 풀이

n = 100
i = 1
num = []
while i**2<n:
    num.append(i**2)
    i+=1
print(num)