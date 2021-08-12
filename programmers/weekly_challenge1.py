price = 3
money = 20
count = 4

def solution(price, money, count):
    return max(0,price*(count+1)*count//2-money)

def solution(price, money, count):
    total_price = 0
    answer = money
    for i in range(1, count+1):
        total_price += price * i
    answer -= total_price

    return abs(min(0, answer))

# 1. 각 횟수별 요금 합계 계산
# 2. money값에서 뺄셈
# 3. 결과 return
# --- 실패 ---
# 1. 테스트 4만 실패
# 2. tot_price < answer 일 경우를 대비해서 abs로 바꿨지만 실패
# 3. 돈이 모자라지 않을 경우 0을 놓침..

abs(-4)
max(0, -4)

max(0,price*(count+1)*count//2-money)

price*(count+1)*count
