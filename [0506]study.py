def solution(n):
    answer = {0}
    
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            print(i)
            # 제곱근까지 약수 더해주기
            answer.add(i)
            # 제곱근부터 약수 더해주기
            answer.add(n//i)
    print(answer)
    return sum(list(answer))

solution(12)



def find_gcd(w,h):
    while w!=0:
        temp=w
        w = h%w
        h = temp
    print(w, h)
    return h

find_gcd(2, 5)

################################
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
    num = math.ceil(h/w) * w // gcd
    return num * gcd

solution(12,8)

# 원래 사각형에서 쓸수 있는 칸 result = w*h
# 대각선의 기울기 = w/h

# 예시의 경우 12/8 = 3/2 = 기존 w, h에서 최대공약수로 나눈 값들임. 그게 최대공약수만큼 반복됨.


# 2x2면 2칸
# 2x3이면 4칸
# 2x4면 

# 5/3

