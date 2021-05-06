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
    gabage = 0
    for i in range(1, w//gcd+1):
        gabage += math.ceil(i*h/w) - math.floor((i-1)*h/w)
        #print(i,'회차',(i*h/w))
        #print(i,'회차',math.ceil(i*h/w))
        #print(i,'회차',math.floor((i-1)*h/w))
        print(i,'회차',gabage)
    gabage *= gcd
    return gabage

find_gabage(8,12)
solution(12,8)

# 원래 사각형에서 쓸수 있는 칸 result = w*h
# 대각선의 기울기 = w/h

# 예시의 경우 12/8 = 3/2 = 기존 w, h에서 최대공약수로 나눈 값들임. 그게 최대공약수만큼 반복됨.


# 2x2면 2칸
# 2x3이면 4칸
# 2x4면 

# 5/3

#####
# 똑똑한 로봇 청소기
###

N = 12  # 총 이동횟수

def move(log):
    # 맨 처음 위치 포함, 13개 지나가면 종료
    if len(log) == N+1:
        return 1

    cnt = 0
    # 전후좌우로 이동
    for d in [[0,1], [0,-1], [1,0], [-1,0]]:
        # 탐색이 안끝나면 계속 이동
        next_pos = [log[-1][0] + d[0], log[-1][1] + d[1]]
        # 로그에 다음 위치가 기록되어있는지 확인하기
        check = False
        for p in log:
            if p[0] == next_pos[0] and p[1] ==next_pos[1]:
                check = True # 있는 경우에 플래그를 True 로 변경
        if check == False:
            cnt += move(log + [next_pos])
    return cnt

print(move([[0, 0]]))
    