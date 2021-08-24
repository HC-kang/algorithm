bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
# 8

bridge_length = 100
weight = 100
truck_weights = [10]
# 101

bridge_length = 100
weight = 100
truck_weights = [10,10,10,10,10,10,10,10,10,10]
#110

def solution(bridge_length, weight, truck_weights):
    answer = 0

    next = truck_weights.pop(0)
    next
    for i in range(len(truck_weights)):
        if next+i < weight:
            next = truck_weights.pop(i)
    
    return answer

def solution(bridge_length, weight, truck_weights):
    answer = 0
    time = 0
    passed = []
    passing = []
    passing
    truck_weights
    while truck_weights:
        if sum(passing) < weight:
            passing.append(truck_weights.pop(truck_weights.index(max(truck_weights))))
        print('passing:', passing)
        print('passed:', passed)
        print('time:', time)
        time+=1

    return answer


# 누가 먼저 가는게 의미가 있나?
# 무거운 게 하나 올라가면 다리는 그냥 사용 불가
# 큰걸 기준으로 넣고, 작은걸 채워넣기 - 제일 큰 것 부터 넣기
