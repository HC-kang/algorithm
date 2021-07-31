
s = 'baabaa' #1
s = 'cdcd' #0

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
    return dic
solution(s)
#=========================================

b = [['12']]
a = '12345'
c = {'12':'', '34':''}
sum(b, [])
a.replace('12','', '34','')
a
b in a
a


def solution(s):
    resul.tag = ''
    while True:
        before = len(result)
        a = [[s[0]] + [s[i] if s[i]!=s[i-1] else '' for i in range(1, len(s))]]
        result = ''
        for i in a:
            result += i
        after = len(result)
        if result =='':
            return 1
        elif after ==before:
            return 0


i = 0
while True:
    i+=1
    print(i)
    if i>=5:
        print('끝')
        break
