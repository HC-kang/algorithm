# 회문

s = 'asdfgfdsa'
def pal(s):
    for i in range(len(s)//2):
        if s[i] == s[-i-1]:
            pass
        else:
            print('회문 아님')
            return
    print('회문임')
pal('assssssssa')


###################


l = list(input())
answer = []
for i in range(ord('a'), ord('z')+1):
    if chr(i) in l:
        answer.append(l.count(chr(i)))
    else:
        answer.append(0)
for i in answer:
    print(i, end=' ')

##################

a = int(input())
b = int(input())
c = int(input())

a = 150
b = 266
c = 427

result = list((str(a*b*c)))
result
for i in range(10):
    if str(i) in result:
        print(result.count(str(i)))
    else:
        print(0)


##########################

l=[]

for i in range(9):
  l.append([])
  for j in range(9):
    if inp[i]!=0:
      l[i].append(0)
      inp[i]-=1
    else:
      l[i].append(1)
k = l[:]


result = 0
for i in range(9):
  for j in range(8):
    count = 0
    if l[j][i]==0:
      for k in range(9-j):
        if l[j+k][i] ==1:
          count+=1
    else:
      continue
    if count>result:
      result = count
print(result)
l



def makeCombi(string, n):
    com = []
    tmp = ''
    if n>len(string):
        return
    elif n==len(string):
        return [string]
    i=0
    j=1
    l=len(string)
    while True:
        tmp+=string[i]
        tmp+=string[j]
        i
        j 
        if (i+n) >= l:
            break
    return com

makeCombi('abc', 2)



def pal(string):
    for i in range(len(string)//2):
        if string[i]==string[-i-1]:
            pass
        else:
            print('회문 아님.')
            return
    return('회문임')

pal('asdfdfdsa')

def pal2(string):
    l = []
    for i in string:
        if i.isalnum():
            l.append(i.lower())
        else:
            pass
    while len(l)>1:
        if l.pop(0) != l.pop():
            print('회문아님.')
            return
    return('회문임.')

pal2('0asdf0fdsa.0!!!!!')

data = '0Mad.am, I\'m! Adam0'
def is_palindrome(data):
    # 전처리
    list_s = []
    for s in data:
        if s.isalnum():
            list_s.append(s.lower())
    while len(list_s) > 1:
        if list_s.pop(0) != list_s.pop():
            print('회문이 아니다!!!!!')
            return
    print('회문이다!!!!!!!!!!!')
is_palindrome(data)

def pal3(string):
    if string == string[::-1]:
        print('회문임')
    else:
        print('회문아님')
pal3('asdfds')

import re

def pal4(string):
    string = string.lower()
    string = re.sub('[^a-z0-9]', '', string)
    if string == string[::-1]:
        print('회문임')
    else:
        print('회문아님')

pal4('asdfds..a')

import collections
deq = collections.deque()

deq.append(0)
deq.appendlegg(0)
deq.pop(0)
deq.popleft(0)

def pal5(string):
    deq = collections.deque()
    for i in string:
        if i.isalnum():
            deq.append(i.lower())
    while len(deq)>1:
        if deq.pop()!=deq.popleft():
            print('회문 아님')
            return
    print('회문임')

pal5('asdfdsa')