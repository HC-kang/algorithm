# 최솟값 찾기 함수
def find_min_idx(a):
    n = len(a)
    min_idx = 0
    for i in range(1, n):
        if a[i] < a[min_idx]:
            min_idx = i
    return min_idx
d = [2,4,5,1,3]
find_min_idx(d)

# 선택정렬 알고리즘
def sel_sort(a):
    result = []
    while a:
        min_idx = find_min_idx(a)
        value = a.pop(min_idx)
        result.append(value)
    return result

d = [2,4,5,1,3]
print(sel_sort(d))


# 선택정렬 알고리즘 2
def sel_sort2(a):
    n = len(a)
    for i in range(0, n-1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]

sel_sort2(d)
print(d)


# 최댓값 찾기 함수
def find_max_idx(a):
    n = len(a)
    max_idx = 0
    for i in range(1, n):
        if a[i] > a[max_idx]:
            max_idx = i
    return max_idx
d = [2,4,5,1,3]
find_max_idx(d)


# 선택정렬 알고리즘 (내림차순)
def sel_sort(a):
    result = []
    while a:
        max_idx = find_max_idx(a)
        value = a.pop(max_idx)
        result.append(value)
    return result

d = [2,4,5,1,3]
print(sel_sort(d))


# 선택정렬 알고리즘 2 (내림차순)
def sel_sort2(a):
    n = len(a)
    for i in range(0, n-1):
        max_idx = i
        for j in range(i + 1, n):
            if a[j] > a[max_idx]:
                max_idx = j
            print(a)
            a[i], a[max_idx] = a[max_idx], a[i]
d=[1,2,3,4,5]
d=[1,5,2,4,3]
sel_sort2(d)
print(d)


# 이분 탐색 알고리즘
def binary_search(a, x):
    start = 0
    end = len(a) -1
    while start<=end:
        mid = (start+end)//2
        if x==a[mid]:
            return mid
        elif x > a[mid]:
            start = mid+1
        else:
            end = mid-1
    return -1
d = [1,4,9,16,25,36,49,64,81]
print(binary_search(d, 36))
print(binary_search(d, 50))


# 이분 탐색 알고리즘(재귀)
def binary_search_sub(a, x):
    start = 0
    end = len(a)-1
    mid = (start+end)//2
    while start<=end:
        if x==a[mid]:
            return a[mid]
        elif x>a[mid]:
            binary_search_sub(a[mid+1:], x)
        else:
            binary_search_sub(a[:mid], x)


d = [1,4,9,16,     25,     36,49,64,81]
print(binary_search_sub(d, 1))
print(binary_search_sub(d, 4))
print(binary_search_sub(d, 9))
print(binary_search_sub(d, 16))
print(binary_search_sub(d, 25))
print(binary_search_sub(d, 36))
print(binary_search_sub(d, 49))
print(binary_search_sub(d, 50))
print(binary_search_sub(d, 64))
print(binary_search_sub(d, 81))
binary_search_sub(d[4:], 49)


# 이분탐색 - 재귀
def binary_search_second(list_a, element, start = 0, end=None):
    end = len(list_a)-1
    mid = (start-end)//2
    if element == list_a[mid]:
        return mid
    elif start > end:
        return None
    elif element > list_a[mid]:
        start = mid+1
    elif element < list_a[mid]:
        end = mid-1
    return binary_search_second(list_a, element, start, end)


d = [1,4,9,16,     25,     36,49,64,81]
print(binary_search_second(d, 1))


def binary_search(element, some_list, start_index=0, end_index=None):
    # end_index가 따로 주어지지 않은 경우에는 리스트의 마지막 인덱스
    if end_index == None:
        end_index = len(some_list) - 1

    middle = (start_index+end_index)//2
  
    # base 바로 찾기
    if element == some_list[middle]:
        return middle # 찾은 인덱스
    # 끝까지 다 돌았는데, 위에서 못찾고 여기 까지 왔을때
    # 주의 !!! start_index == end_index 아님!!! 재귀무한루프걸림  
    elif start_index > end_index: # 비정상 상태
        return # None
    # 재귀로 쪼개서 들어가기
    elif element > some_list[middle]:
        start_index = middle + 1
    elif element < some_list[middle]:
        end_index = middle - 1
    return binary_search(element, some_list, start_index, end_index)

print(binary_search(2, [2, 3, 5, 7, 11])) # => 0
print(binary_search(5, [2, 3, 5, 7, 11])) # => 2
print(binary_search(11, [2, 3, 5, 7, 11])) # => 4
print(binary_search(0, [2, 3, 5, 7, 11])) # none
print(binary_search(13, [2, 3, 5, 7, 11])) # none


def binary_search(element, some_list, start_index=0, end_index=None):
    # end_index가 따로 주어지지 않은 경우에는 리스트의 마지막 인덱스
    if end_index == None:
        end_index = len(some_list) - 1
    # base 1 경우 해당 값 못찾기 - 못찾는 상황은 시작>마지막 조건일때
    # start_index가 end_index보다 크면 some_list안에 element는 없다
    if start_index > end_index:
        return None
    # base 2 경우 해당 값찾기  
    # 범위의 중간 인덱스를 찾기
    mid = (start_index + end_index) // 2

    # 이 인덱스의 값이 찾는 값인지 확인
    if some_list[mid] == element:
        return mid

    # 찾는 항목이 중간 값보다 작으면 리스트 왼쪽을 탐색
    if element < some_list[mid]:
        return binary_search(element, some_list, start_index, mid - 1)
    # 찾는 항목이 중간 값보다 크면 리스트 오른쪽을 탐색
    else:
        return binary_search(element, some_list, mid + 1, end_index)  


#################################################