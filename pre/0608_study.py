a = list(range(10))

print(a)


b = [i for i in range(10) if i%2==0]
b

c = [[0]*3 for _ in range(10)]
c[2][2] = 1
c

d = [[0]*4]*6
d
d[2][2]=1

e = [[1,2,3]]*5
e
e[3][1] = 1000

f = [[0]] * 20
f
f[2][0] = 1

for _ in range(10):
    print(_)

a = {1,2,3}
b = {3,4,5}
a
b
a | b


import sys

data = sys.stdin.readline().strip()
print(data)
a = '0010'
print(f'print({a})')


pow(2, 5)


from sympy import Limit, S, Symbol
x = Symbol('x')

Limit(1/x, x, S.Infinity).doit()

Limit(1/x, x, S.Infinity, dir = '-').doit()

arr = [1,2,3]
answer = [arr[0]]
answer

b = (1,2,3)
b

###########
n, k = map(int, input().split())
cnt = 0
while n != 1:
    if n % k == 0:
        n //= k
        cnt+=1
    else:
        n-=1
        cnt+=1
print(cnt)

###############

S = list(input())
result = 1
if S[0]!='1':
    result = 1
elif S[0]=='1':
    result = 0
for i in S:
    if int(i)==0 or int(i)==1:
        result += int(i)
    else:
        result *= int(i)
print(result)