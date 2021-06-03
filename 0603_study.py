def mapper(n): # 각 숫자를 좌표로 바꿔주는 함수
    dicts = {'*': [3,0], 0:[3,1], '#':[3,2]}
    if n=='*' or n==0 or n=='#':
        return dicts[n]
    else:
        x = (n-1) // 3
        y = (n-1) % 3
    return [x, y]

def calc_dist(A, B): # 두 좌표 간 거리를 계산하는 함수
    distance = sum([abs(a-b) for a, b in zip(A, B)])
    return distance

    
def solution(numbers, hand): # 본체
    result = []
    L = [1,4,7]
    R = [3,6,9]
    
    L_loc = [3,0]
    R_loc = [3,2]
    
    main_hand = (hand[0]).upper()
    
    for i in numbers:
        if i in L:
            result.append('L')
            L_loc = mapper(i)
        elif i in R:
            result.append('R')
            R_loc = mapper(i)
        else:
            L_dist = calc_dist(mapper(i), L_loc)
            R_dist = calc_dist(mapper(i), R_loc)
            if L_dist<R_dist:
                result.append('L')
                L_loc = mapper(i)
            elif R_dist<L_dist:
                result.append('R')
                R_loc = mapper(i)
            else:
                if main_hand=='L':
                    result.append('L')
                    L_loc = mapper(i)
                else:
                    result.append('R')
                    R_loc = mapper(i)
    return ''.join(result)


# 1, 4, 7 ? L
# 3, 6, 9 ? R
# 2,5,8,0 ? 
# 거리 ? 
# 같음? S
# 다름? L, R

# 맨 처음 2, 5, 8, 0은 왼손/오른손잡이로 결정? 아님. 이전 번호.
# 거리가 같으면 우선쓰는 손이 감.


##########
import re 

new_id = '...!@BaT#*..y.abcdefghijklm'
step1 = ''
for c in new_id:
    if c.isalpha:
        step1 += c.lower()
    else:
        step1 += c
print(step1)

step2 = ''
lists = list('`$()*+?[]!@#\^{}')
for c in step1:
    if c in lists:
        pass
    else:
        step2 += c
print(step2)

step3 = re.sub('(([.])\\2{1,})', '.', step2)

if step3[0]=='.':
    step4 = step3[1:]
elif step3[-1]=='.':
    step4 = step3[:-1]
else:
    step4 = step3

if step4 == '':
    step5 = step4+'a'
else:
    step5 = step4

if len(step5) >=16:
    step6 = step5[:16]
    if step6[:-1]=='.':
        step6 = step6[:-1]

if len(step6)<=2:
    while len(step6)<=3:
        step6+='.'
step7 = step6

print(step7)



step5 = 'abcdefghijklmn.p'

if len(step5) >=16:
    step6 = step5[:15]
else:
    step6 = step5
print(step6)
if step6[-1]=='.':
    step6 = step6[:-1]
print(step6)


########################
def solution(new_id):            
    step1 = ''
    for c in new_id:
        if c.isalpha:
            step1 += c.lower()
        else:
            step1 += c

    step2 = ''
    lists = list('abcdefghijklmnopqrstuvwxyz0123456789-_.')
    for c in step1:
        if c not in lists:
            pass
        else:
            step2 += c

    while '..' in step2:
        step2 = step2.replace('..', '.')
    step3 = step2

    if step3[0]=='.':
        step4 = step3[1:]
    elif step3[-1]=='.':
        step4 = step3[:-1]
    else:
        step4 = step3

    if step4 == '':
        step5 = step4+'a'
    else:
        step5 = step4
    
    step6 = ''
    if len(step5) >=16:
        step6 = step5[:15]
    else:
        step6 = step5
    
    if step6[-1]=='.':
        step6 = step6[:-1]
    
    if len(step6)<=2:
        while len(step6)<3:
            k = step6[-1]
            step6+=k
    step7 = step6
    return step7

####################################

import re
new_id = '...!@BaT#*..y.abcdefghijklm'

def solution1(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st

solution1(new_id)