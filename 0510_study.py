# 퀵 정렬
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

d = [6,8,3,9,10,1,2,4,7,5,5]
quick_sort(d)


# 퀵 정렬2
def quick_sort_sub(a, start, end):
    # 종료 조건 : 정렬 대상이 1개 이하이면 정렬할 필요 없음.
    if end-start<=0:
        return
    # 기준 값을 정하고 기준 값에 맞춰 리스트 안에서 각 자료의 위치를 맞춤
    # [기준 값보다 작은 값들, 기준 값, 기준 값보다 큰 값들]
    pivot = a[end] # 편의상 리스트의 마지막 값을 기준값으로 정함
    i = start
    for j in range(start, end):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[end] = a[end], a[i]
    # 재귀 호출 부분
    quick_sort_sub(a, start, i-1) # 기준 값보다 작은 그룹을 재귀 호출로 다시 정렬
    quick_sort_sub(a, i+1, end)   # 기준 값보다 큰 그룹을 재귀 호출로 다시 정렬

# 리스트 전체(0~ lend(a)-1)를 대상으로 재귀 호출 함수 호출
def quick_sort2(a):
    quick_sort_sub(a, 0, len(a)-1)

d = [6,8,3,9,10,1,2,4,7,5,5]
quick_sort2(d)
print(d)


list1.remove('m')
list1 = ['m', 's', 'a', 'm']
list2 = ['s', 'a', 'm']
for i in list1:
    for j in list2:
        if i==j:
            print(list1)
            print(list2)
            list1.remove(i)
            print(list1)
            print(list2)
            print()
            
print(list1)
print(list2)