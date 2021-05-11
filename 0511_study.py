def solution(n):
    return int((n**0.5+1)**2 if (n**0.5)%1==0 else -1)

solution(121)
solution(9)
solution(16)
solution(9)

############################
# 퀵소트

# 범위를 지정하여 정렬하는 재귀 호출함수
def quick_sort_sub(a, start,end):
    # 종료 조건 ; 정렬 대상이 1개 이하면 정렬할 필요 없음
    if end-start <= 0:
        return
    # 기준값을 정하고 기준값에 맞춰 리스트 안에서 각 자료의 위치를 맞춤
    # 기준 값보다 작은 값들, 기준 값, 기준 값보다 큰 값들
    pivot = a[end] # 편의상 리스트의 마지막 값을 기준값으로 정함
    i = start
    for j in range(start, end):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[end] = a[end], a[i]