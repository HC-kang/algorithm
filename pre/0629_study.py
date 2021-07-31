def solution(s):
    dic = ['aa','bb','cc','dd','ee','ff','gg','hh','ii','jj','kk','ll','mm',
           'nn','oo','pp','qq','rr','ss','tt','uu','vv','ww','xx','yy','zz']
    while True:
        before = len(s)
        for i in dic:
            s = s.replace(i, '')
        after = len(s)
        if before == after:
            return 0
        elif s=='':
            return 1


s1 = 'baabaa' # 1
s2 = 'cdcd' # 0






import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 0, 0.1

s = np.random.normal(mu, sigma, 1000)
s

plt.figure(figsize = (15, 7))
plt.plot(s)

count, bins, ignored = plt.hist(s, 30, normed
=True)

plt.plot(bins, 1/(sigma * np.sqrt(2*np.pi))*np.exp(-(bins-mu)**2/2*(sigma)))

########################################################################################################

# 세 정수를 입력받아 최댓값 구하기
print('최댓값 구하기')
a = int(input('a의 값'))
b = int(input('b의 값'))
c = int(input('c의 값'))

maximum = a
if b> maximum: maximum = b
if c> maximum: maximum = c

print(f'최댓값은 {maximum}')

############################################################################################################
print('이름을 입력하세요 : ', end = '')
name= input()
print(f'안녕하세요? {name}님')

##############################################################################

name = input('이름?:')
print(f'안녕하세요? {name}님')

##############################################################################

int('17')

int('110', 2)

##############################################################################

def max3(a,b,c):
    maximum = a
    if b>maximum: maximum=b
    if c>maximum: maximum=c
    return maximum

print(f'max3(3,2,1) = {max3(3,2,1)}')
print(f'max3(3,2,3) = {max3(3,2,3)}')
print(f'max3(3,2,4) = {max3(3,2,4)}')
print(f'max3(3,2,5) = {max3(3,2,5)}')
print(f'max3(3,2,6) = {max3(3,2,6)}')
print(f'max3(3,2,7) = {max3(3,2,7)}')
print(f'max3(3,7,8) = {max3(3,7,8)}')
print(f'max3(3,9,1) = {max3(3,9,1)}')
print(f'max3(3,4,1) = {max3(3,4,1)}')

##############################################################################

def med3(a,b,c):
    if a>=b:
        if b>=c:
            return b
        elif c>=a:
            return a
    elif a>c:
        return a
    elif b>c:
        return c
    else:
        return b

print('세 정수의 중앙값')
a = int(input('a'))
b = int(input('b'))
c = int(input('c'))

print(f'중앙값 {med3(a,b,c)}')
