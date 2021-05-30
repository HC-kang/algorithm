from sympy import expand, factor, Symbol

x = Symbol('x')

expand((x+1)*(x+2))

factor(x**2+3*x+2)


a, b, c = map(int, input().split())
if a%2==0:
    print(a)
if b%2==0:
    print(b)
if c%2==0:
    print(c)


a = 1
while a!=0:
    a = int(input())
    if a==0:
        break
    print(a)