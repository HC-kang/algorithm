print('a부터 b까지 정수의 합을 구합니다')
a = int(input('정수 a : '))
b = int(input('정수 b : '))

if a>b:
    a, b = b, a

sum = 0
for i in range(a, b+1):
    sum+=i

print(f'{a}부터 {b}까지의 합은 {sum} 입니다.')

################################################

a = int(input('몇 번?'))
for i in range(a):
    if i%2==0:
        print('+', end = '')
    else:
        print('-',end = '')

################################################


for i in range(100):
    if i%10==0:
        print(i)
    else:
        print(i, end = ' ')

for i in range(10):
    print()
    for j in range(1, 10):
        print((str(10*i+j)).zfill(2), end = ' ')

id(a)
id(12)
id(3)

tuple00  = tuple()
tuple01 = 1,
tuple00
tuple01
tuple00 + tuple01

from typing import Any, Sequence
