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