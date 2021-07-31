#####
# 재귀호출을 통한 이분탐색
###

def binary_search_sub(a, x, start, end):
    # 종료조건 설정

    if start>end:
        return -1
    mid = (start +end) //2
    if x == a[mid]:
        return mid
    elif x > a[mid]:
        return binary_search_sub(a, x, mid+1, end)
    else:
        return binary_search_sub(a, x, start, mid-1)
    
    return -1

def binary_search(a, x):
    return binary_search_sub(a, x, 0, len(a)-1)

d = [1, 4, 9, 16, 25, 36, 49, 64, 81]

binary_search(d, 16)

######################

#####
# 삽입 정렬
###

def insertion_sort(data):
    for index in range(len(data)-1):
        for index2 in range(index+1, 0, -1):
            if data[index2]<data[index2-1]:
                data[index2], data[index2-1] = data[index2-1], data[index2]
            else:
                break
    return data

import random
data_list = random.sample(range(100), 50)
data_list
print(insertion_sort(data_list))

# 2

# 리스트 r에서 v 가 들어가야 할 위치를 돌려주는 함수
def find_ins_idx(r, v):
    # 이미 정렬된 리스트 r의 자료를 앞에서부터 확인
    for i in range(0, len(r)):
        # v 값보다 i번 위치에 있는 자료값이 크면
        # v가 그 앞으로 놓여야 함. 
        if v < r[i]:
            return i
    # 적절한 위치를 못 찾았을 경우 v 가 r의 모든 원소보다 크다는 뜻이니 맨 뒤로 삽입
    return len(r)

def ins_sort(a):
    result=[]       # 새 리스트에 정렬된 값 저장
    while a:        # 기존 리스트에 값이 남아있으면 계속 반복
        value = a.pop(0)        # 기존 리스트에서 첫번째 값 꺼냄
        ins_idx = find_ins_idx(result, value)       # 꺼낸 값이 들어갈 위치 찾기
        result.insert(ins_idx, value)       # 찾은 위치에 값 삽입(이후 값은 한 칸씩 밀려남)
    return result

d = [2,4,5,1,3]
print(ins_sort(d))

# 3

# 일반적인 삽입 정렬
def ins_sort(a):
    n = len(a)
    for i in range(1, n):        # 1부터 n-1까지
        # i번 위치의 값을 key로 지정
        key = a[i]
        # j를 i바로 왼쪽으로 저장
        j = i-1
        # 리스트의 j번 위치에 있는 값과 key를 비교해 key가 삽입될 적절한 위치를 찾음
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]   # 삽입할 공간이 생기도록 값을 오른쪽으로 한 칸 이동
            j-=1
        a[j+1] = key    # 찾은 삽입 위치에 key를 저장

d = [2, 4, 5, 1, 3]
ins_sort(d)
print(d)

# 4 내림차순 삽입 정렬

def ins_sort_down(a):
    n = len(a)
    for i in range(1, n):        # 1부터 n-1까지
        # i번 위치의 값을 key로 지정
        key = a[i]
        # j를 i바로 왼쪽으로 저장
        j = i-1
        # 리스트의 j번 위치에 있는 값과 key를 비교해 key가 삽입될 적절한 위치를 찾음
        while j >= 0 and a[j] < key:
            a[j+1] = a[j]   # 삽입할 공간이 생기도록 값을 오른쪽으로 한 칸 이동
            j-=1
        a[j+1] = key    # 찾은 삽입 위치에 key를 저장

d = [2, 4, 5, 1, 3]
ins_sort_down(d)
print(d)



