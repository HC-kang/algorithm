from typing import Any, MutableSequence

def reverse_array(a: MutableSequence) -> None:
    '''뮤터블 시퀀스 a의 우너소를 역순으로 정렬'''
    n = len(a)
    for i in range(n//2):
        a[i], a[n-i-1] = a[n-i-1],a[i]

if __name__ == '__main__':
    print('배열 원소를 역순으로 정렬합니다.')
    nx = int(input('원소 수를 입력하세요. :'))
    x = [None]*nx # 원소 수 nx인 리스트 생성

    for i in range(nx):
        x[i] = int(input(f'x[{i}] 값을 입력하세요.:'))

    reverse_array(x)

    print('배열 원소를 역순으로 정렬')
    for i in range(nx):
        print(f'x[{i}] = {x[i]}')


list1 = [2,5,1,3,9,6,7]
list1.reverse()
list1

list2 = reversed(list1)
list2

tuple1 = (2,5,1,3,9,6,7)
tuple2 = reversed(tuple1)
print(tuple(tuple2))
