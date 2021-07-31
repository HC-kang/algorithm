lists = ['hi', 'hello']

''.join(lists,)


###############
def solution(s):
    answer=''
    cnt=0
    for i in s:
        if i==' ':
            answer += ' '
            cnt-=1
        elif cnt%2:
            answer +=i.lower()
            cnt+=1
        else:
            answer +=i.upper()
            cnt+=1
    return answer

def solution(s):
    lists=[]
    answer = ''
    cnt=0
    for i in s:
        lists.append(i)
    for j in lists:
        if j==' ':
            answer = answer + ''
            cnt=1
        if cnt%2:
            answer = answer + j.lower()
            cnt+=1
        else:
            answer = answer + j.upper()
            cnt+=1
    return answer


def solution(s):
    return ' '.join([''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(w)]) for w in s.split(' ')])

s.split(' ')
answer
lists
ord(' ')

answer = 'h'
answer = answer.join('hi')
answer
ss.index('try')
ss = s.split()
s="try hello world     try hello worldtry hello world"
solution(s)

# return "TrY HeLlO WoRlD"

a = 'try'
for i in range(1):
a = a+'i'
a

k = ['try', 'hello', 'world']
' '.join(k)

aa = ['가' , '나','마', '라']
sorted(aa)
aa
aa.sort()