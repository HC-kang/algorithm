###############################################################################
    #####
    # 최대공약수 최소공배수 구하기
    ###
    ### 내 풀이
def solution(n, m):
    answer = []
    k=m*n
    while m!=0:
        temp=m
        m = n%m
        n = temp
    answer.append(n)
    answer.append(k//n)
    return answer

########################
########################

        ### 1
def gcd(a, b):
    return b if a % b == 0 else gcd(b, a % b)

def lcm(a, b):
    return int(a * b / gcd(a, b))

def gcdlcm(a, b):
    answer = [gcd(a,b), lcm(a,b)]

    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(gcdlcm(3,12))

# memo
# 진짜 깔끔하고 이해하기 쉽게 하나씩 함수로 지정해서 불러옴. 대단.. 

########################

        ### 2
def gcdlcm(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(a*b/c)]

    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(gcdlcm(3,12))

# memo
# 조건문을 그냥 max, min으로 퉁쳐버려서 코드가 훨씬 깨끗.
# 그리고 나는 후반 int(a*b)/c 때문에 변수 k를 다시 또 추가해줬는데
# 그렇게 번거롭지 않게 두 가지 문제를 한번에 처리했음.  

###############################################################################
    #####
    # 소수 찾기
    ###
    ### 내 풀이
def solution(n):
    check = [True]*(n+1)
    check[0] = False
    check[1] = False
    for i in range(2, int(n**0.5)+1):
        if check[i] == True:
            j=2
            while j*i <= n:
                check[i*j] =False
                j+=1
    return check.count(True)

########################
########################


def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)

# memo
# 리스트 말고 세트로 푸는 아이디어를 잠깐 생각은 했었는데 결국은 못 만들었는데, 이 풀이에서 만들어줌.


###############################################################################
    #####
    # 문자열을 정수로 변경
    ###
    ### 내 풀이
def solution(s):
    return int(s)

########################
########################

def strToInt(str):
    result = 0

    for idx, number in enumerate(str[::-1]):
        if number == '-':
            result *= -1
        else:
            result += int(number) * (10 ** idx)

    return result

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(strToInt("-1234"));


# memo
# 이게뭐지,, 누가 골드버그 기계라고 하네. 근데 참 신기한 아이디어긴 하다.


###############################################################################
    #####
    # 서울에서 김서방 찾기
    ###
    ### 내 풀이
def solution(seoul):
    anser = ''
    idx = 0
    for i in range(1000):
        if seoul[idx] == 'Kim':
            answer =  idx
        else:
            idx+=1
    return '김서방은 {}에 있다'.format(answer)

########################
########################

        ### 1
def findKim(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))

# 실행을 위한 테스트코드입니다.
print(findKim(["Queen", "Tod", "Kim"]))

# memo
# 생각없이 for 부터 갈기고 보는 버릇좀 어떻게 해야겠다. index라는게 있는데 왜 써먹질 못하고,,
# 심지어 모르는것도 아닌데 써먹을 생각조차 안했다.



########################
###############################################################################
    #####
    # 시저 암호
    ###
    ### 내 풀이

def solution(s, n):
    ord_list = []
    answer = []
    for char in list(s):
        if char == " ":
            ord_list.append(ord(char))
        elif (97 <= ord(char) <=122):
            if 122 < (ord(char)+n):
                ord_list.append(ord(char)+n-26)
            else:
                ord_list.append(ord(char)+n)
        elif (65<= ord(char) <= 90):
            if 90 < (ord(char)+n):
                ord_list.append(ord(char)+n-26)
            else:
                ord_list.append(ord(char)+n)
    for i in ord_list:
        answer.append(chr(i))
    return ''.join(answer)

########################
########################

        ### 1
def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)
    # 주어진 문장을 암호화하여 반환하세요.


# 실행을 위한 테스트코드입니다.
print('s는 "a B z", n은 4인 경우: ' + caesar("a B z", 4))

# memo
# 내가 ord 와 chr를 써서 가고자 했던 방향의 최종답안인듯.
# 내가 코드 숫자를 가지고 지저분하게 if 문까지 써가면서 난리친거를 이렇게 간단하게
# .isupper 와 .islower를 써서 구분하다니. 이전에 와일문을 조건문으로 쓰는것도 참
# 대단하다고 생각했는데 이런부분, 그러니까 if 문을 줄여서 코드를 간단하게 만드는 스킬이
# 정말 대단한듯. 

########################
########################

        ### 1
def solution(s, n):
    answer = ''

    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = lower.upper()

    for alphabet in s:

        if alphabet in lower:
            idx = lower.index(alphabet) + n
            answer += lower[idx % 26]

        elif alphabet in upper:
            idx = upper.index(alphabet) + n
            answer += upper[idx % 26]

        else:
            answer += ' '
    
    return answer

# memo
# 뭔가 정말,, 기초적인 원리는 위와 같은 느낌인데 ord나 chr 없이 인덱스만 가지고 간단하게 정리.
# 무엇보다 정말 처음보는사람도 대충 무슨소린지 알아들을 수 있는 간결함이 대단한듯. 

########################
########################
###############################################################################
    #####
    # 멀쩡한 사각형
    ###
    ### 내 풀이

import math
def solution(w,h):
    if w>h:
        w, h = h, w
    answer = w*h - find_gabage(w, h)
    return answer

def find_gcd(w,h):
    while w!=0:
        temp = w
        w = h%w
        h = temp
    return h

def find_gabage(w, h):
    gcd = find_gcd(w, h)
    gabage = 0
    for i in range(1, w//gcd+1):
        gabage += math.ceil(i*h/w) - math.floor((i-1)*h/w)
    gabage *= gcd
    return gabage


########################
########################

        ### 1
def gcd(a,b): return b if (a==0) else gcd(b%a,a)    
def solution(w,h): return w*h-w-h+gcd(w,h)

# memo
# 처음엔 진짜 걍 물음표,,,
# 근데 이건 정말 코딩보다도 머리쓰기의 문제라는게 참 대단하게 느껴졌다.
# 내가 이걸 풀었을때도 기분 좋았지만
# 내가 이 답안을 보고 멍청하게 느껴졌음에도 이건 너무 기분이 좋다
# 이런 풀이가 앞으로도 많았으면. 

########################






















########################
###############################################################################
    #####
    # 제목
    ###
    ### 내 풀이

def solution

########################
########################

        ### 1
def f

# memo
# 진

########################