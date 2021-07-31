def quick_sort(a):
    n = len(a)
    # 종료 조건 : 정렬할 리스트의 자료 개수가 한 개 이하이면 정렬할 필요가 없음.
    if n <= 1:
        return a
    # 기준 값을 정하고 기준에 맞춰 그룹을 나누기
    pivot = a[-1]   # 편의상 리스트의 마지막 값을 기준 값으로 정함
    g1 = [] # 그룹 1: 기준 값보다 작은 값을 담을 리스트
    g2 = [] # 그룹 2: 기준 값보다 큰 값을 담을 리스트
    for i in range(0, n-1): # 마지막 값은 기준 값이므로 제외
        if a[i] < pivot:  # 기준 값과 비교
            g1.append(a[i]) # 작으면 g1에 추가
        else:
            g2.append(a[i]) # 크면 g2에 추가
    # 각 그룹에 대해 재귀 호출로 퀵 정렬을 한 후
    # 기준 값과 합쳐 하나의 리스트로 결괏값 반환
    return quick_sort(g1) + [pivot] + quick_sort(g2)

################

def quick_sort(a):
    n = len(a)
    if n <= 1:
        return a
    pivot = a[-1]
    g1, g2 = [], []
    for i in range(0, n-1):
        if a[i] < pivot:
            g1.append(a[i]) 
        else:
            g2.append(a[i])
    return quick_sort(g1) + [pivot] + quick_sort(g2)



d = [4,3,5,6,7,8,2,3,4,5,3,1,2,2]
quick_sort(d)
d



def solution(arr):
    min = 0
    if len(arr) == 1:
        return [-1]
    else:
        for a in arr:
            if a>min
    return answer



############################################
def quick_sort(a):
    n = len(a)
    if n <= 1:
        return a
    pivot = a[-1]
    g1 = []
    for i in range(0, n-1):
        if a[i] < pivot:
            g1.append(a[i])
    return quick_sort(g1)[0]

d = [4,3,5,6,7,8,2,3,4,5,3,1,2,2]
a = (d.remove(4))
d
a

################

def quick_sort(a):
    n = len(a)
    if n <= 1:
        return a
    pivot = a[-1]
    g1 = []
    g2 = []
    for i in range(0, n-1):
        if a[i] < pivot:
            g1.append(a[i])
        else:
            g2.append(a[i]) 
    return quick_sort(g1) + [pivot] + quick_sort(g2)
    
def solution(arr):
    answer = arr
    if len(arr) <= 1:
        return [-1]
    else:
        answer.remove(quick_sort(arr)[0])
    return answer

solution([4,3,2,1])
quick_sort([4,3,2,1])

a = [4,3,2,1]
quick_sort(a)