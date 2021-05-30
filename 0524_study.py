def quick_sort_sub(a, start, end):
    if end - start <= 0:
        return
    pivot = a[end]
    i = start
    for j in range(start, end):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[end] = a[end], a[i]
    # 재귀 호출 부분
    quick_sort_sub(a, start, i-1)
    quick_sort_sub(a, i+1, end)

def quick_sort(a):
    quick_sort_sub(a, 0, len(a)-1)

d = [6, 8, 3, 9, 10, 1,2,4, 7, 5]
quick_sort(d)
print(d)


#########################

def bubble_sort(a):
    n = len(a)
    while True:
        changed = False
        for i in range(0, n-1):
            if a[i] > a[i+1]:
                print(a)  # 참고용
                a[i], a[i+1] = a[i+1], a[i]
                changed = True
        if changed == False:
            return

d = [11,2,4,5,1,3,9,8,7,6,10]
bubble_sort(d)
print(d)

#############

a, b = map(int, input().split())
print(a,b)

a, b = map(int, input().split())

print(a<b)

a = int(input())
print(not bool(a))

 a = 100
 ~a