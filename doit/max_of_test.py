# 각 배열 원소의 최댓값을 구해 출력하기(tuple, str, list)

from max import max_of

t = (4,7, 5.6, 2, 3.14, 1)
s = 'string'
a = ['DTS', 'AAC', 'FLAC']

print(f'{t}의 최댓값은 {max_of(t)}입니다.')
print(f'{s}의 최댓값은 {max_of(s)}입니다.')
print(f'{a}의 최댓값은 {max_of(a)}입니다.')


lst1 = [1,2,3,4,5]
lst2 = [1,2,3,4,5]

lst1==lst2
lst1 is lst2


for i, j in enumerate(lst1):
    print(f'index: {i+1}, values:{j}')