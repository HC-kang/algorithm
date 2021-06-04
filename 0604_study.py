def solution(N, stages):
    tmp = [0]
    answer = []
    for i in range(1, N+1):
        if i in stages:
            tmp.append(len([x for x in stages if x==i])/(len([x for x in stages if x>=i])))
        else:
            tmp.append(0)
    _tmp = list(enumerate(tmp))[1:]

    for i in range(len(_tmp)-1):
        max_idx = i
        for j in range(i+1, len(_tmp)):
            if _tmp[j][1] >_tmp[max_idx][1]:
                max_idx = j
        _tmp[i], _tmp[max_idx] = _tmp[max_idx], _tmp[i]
    _tmp
    for i in range(len(_tmp)):
        answer.append(_tmp[i][0])

    return answer




N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

N = 4
stages = [4,4,4,4,4]

tmp = [0]
answer = []
# 값 구하기
for i in range(1, N+1):
    if i in stages:
        tmp.append(len([x for x in stages if x==i])/(len([x for x in stages if x>=i])))
    else:
        tmp.append(0)
_tmp = list(enumerate(tmp))[1:]

__tmp = []
print(_tmp)
for i in range(1, len(_tmp)+1):
    maxint = -1
    for j in range(1, len(_tmp)+1):
        if _tmp[-j][1] >= _tmp[maxint][1]:
            maxint = -j
        print('_tmp:', _tmp)
        print('__tmp:', __tmp)
    __tmp.append(_tmp[maxint][0])
    _tmp.remove(_tmp[maxint])

__tmp



# 선택정렬 알고리즘 2
def sel_sort2(a):
    n = len(a)
    for i in range(0, n-1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]







solution(5, [2, 1, 2, 6, 2, 4, 3, 3])
solution(4, [4,4,4,4,4])


dict = {1:5, 2:4, 3:3, 4:2, 5:1}
dict.sort_index()





#################

import math

from numpy.lib import financial 
loc = {1:[0,0], 2:[0,1], 3:[0,2], 4:[1,0], 5:[1,1], 6:[1,2], 7:[2,0], 8:[2,1], 9:[2,2], '*':[3,0], 0:[3,1], '#':[3,2]}
answer_L = ['*']
answer_R = ['#']
def dis(a, b) : 
    return math.sqrt((loc[a][0]-loc[b][0])**2 + (loc[a][1]-loc[b][1])**2)


def solution(numbers, hand):
    for i in numbers :

        print(answer_L[-1])
        print(answer_R[-1])
        if i == 1 or i == 4 or i == 7 : answer_L.append(i)
        elif i == 3 or i == 6 or i == 9 : answer_R.append(i)
        elif dis(answer_L[-1], i) < dis(answer_R[-1], i) : answer_L.append(i)
        elif dis(answer_L[-1], i) > dis(answer_R[-1], i) : answer_R.append(i)
        elif dis(answer_L[-1], i) == dis(answer_R[-1], i) : 
            if hand == 'right' : answer_R.append(i)
            elif hand == 'left' : answer_L.append(i)
        print('시행 :',i)
        print(answer_L)
        print(answer_R)
        print('좌우')



solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	,	"right")



###########

n = 45
ans = ''
while n>3:
    m = n%3
    n = n//3
    ans = ans+str(m)

ans = ans+str(n)    
print('답:',ans)
int(ans, 3)


def solution(n):
    answer = ''
    while n>=3:
        m = n%3
        n = n//3
        answer = answer+str(m)
    answer = answer+str(n)    
    answer = int(answer, 3)
    return answer

solution(1) 


#############################

def solution(N, stages):
    tmp = [0] # 인덱스 1부터 시작하게 장난질
    # 실패율을 계산
    for i in range(1, N+1):
        if i in stages:
            tmp.append(len([x for x in stages if x==i])/(len([x for x in stages if x>=i])))
        else:
            tmp.append(0)
    # 인덱스 지정
    _tmp = list(enumerate(tmp))[1:]
    # 점수 높은순으로 정렬
    __tmp = []
    for i in range(1, len(_tmp)+1):
        maxint = -1
        for j in range(1, len(_tmp)+1):
            if _tmp[-j][1] >= _tmp[maxint][1]:
                maxint = -j
        __tmp.append(_tmp[maxint][0])
        _tmp.remove(_tmp[maxint])
    return __tmp



N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

N = 4
stages = [4,4,4,4,4]

solution(5, [2, 1, 2, 6, 2, 4, 3, 3])


def solution(N, stages):
    fail = {}
    for i in range(1,N+1):
        try:
            fail_ = len([a for a in stages if a==i])/len([a for a in stages if a>=i])
        except:
            fail_ = 0
        fail[i]=fail_
    answer = sorted(fail, key=fail.get, reverse=True)
    return answer

