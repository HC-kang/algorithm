def palindrome(s):
    # 큐와 스택을 리스트로 정리
    qu = []
    st = []
    # 1단계 : 문자열의 알파벳 문자를 각각 큐와 스택에 넣기
    for x in s:
        # 해당 문자가 알파벳이면( = 공백, 특수문자, 숫자가 아니면)
        # 쿠와 스택에 각각 그 문자를 추가
        if x.isalpha():
            qu.append(x.lower())
            st.append(x.lower())
    # 2단계 : 큐와 스택에 들어있는 문자를 꺼내며 비교
    while qu:
        if qu.pop(0) != st.pop():
            return False
    
    return True

print(palindrome('Wow'))
print(palindrome("Madam, I'm Adam"))
print(palindrome('Madam, I am Adam'))


def check(s):
    a=''
    b=''
    for k in s:
        if k.isalpha():
            b+=k.lower()
    s = s.lower()
    for i in range(len(s)-1, 0-1, -1):
        if s[i].isalpha():
            a+=s[i].lower()
    print(a, b)
    if a != b:
        return False
    
    return True


print(check('Wow'))
print(check("Madam, I'm Adam"))
print(check('Madam, I am Adam'))

def palindrome2(s):
    i=0             # 문자열의 앞에서 비교할 위치
    j=len(s) - 1    # 문자열의 뒤에서 비교할 위치
    while i<j:      # 중간까지만 검사하면 됨.
        # i 위치에 있는 문자가 알파벳 문자가 아니면 뒤로 이동
        if s[i].isalpha() == False:
            i += 1
        # j 위치에 있는 문자가 알파벳 문자가 아니면 앞으로 이동
        elif s[j].isalpha() == False:
            j -= 1
        # i, j위치 둘 다 알파벳 문자가 있으면 두 문자를 비교하고 다르면 회문이 아님.
        elif s[i].lower() != s[j].lower():
            return False
        # i 와 j 위치에 두 문자를 비교하고 같우면 다음 비교대상으로 이동
        else:
            i += 1
            j -= 1
    return True

print(palindrome2('Wow'))
print(palindrome2("Madam, I'm Adam"))
print(palindrome2('Madam, I am Adam'))


#####
# 병합정렬 알고리즘
###
def merge_sort(a):
    n = len(a)
    # 종료 조건 : 정렬할 리스트의 자료 개수가 한 개 이하이면 정렬할 필요 없음.
    if n <= 1:
        return a
        ## 재귀함수는 종료조건을 '반복문의 종료' 가 아니라 함수 자체에 넣어줌.
    # 그룹을 나누어 각각 병합정렬을 호출
    mid = n//2 # 중간을 기준으로 두 그룹으로 나눔
    g1 = merge_sort(a[:mid]) # 재귀 호출로 첫 번째 그룹 정렬
    g2 = merge_sort(a[mid:]) # 재귀 호출로 두 번째 그룹 정렬
    # 두 그룹을 하나로 병합
    result = [] # 두 그룹을 합쳐 만들 최종결과
    while g1 and g2: # 두 그룹에 모두 자료가 남아있는 동안 반복
        if g1[0] < g2[0]: # 두 그룹의 맨 앞 자료 값을 비교
            result.append(g1.pop(0))
        else:
            # g2의 값이 더 작으면 그 값을 빼내어 결과로 추가
            result.append(g2.pop(0))
    while g1:
        result.append(g1.pop(0))
    while g2:
        result.append(g2.pop(0))
    return result

merge_sort([1,9,8,7,6,5,4,3,2,2,2,2,2])


# 일반적인 병합정렬
def merge_sort2(a):
    n = len(a)
    # 종료 조건 : 정렬할 리스트의 자료 개수가 한 개 이하일 땐 정렬할 필요가 없음.
    if n <=1:
        return
    # 그룹을 나누어 각각 병합정렬 호출
    mid = n//2
    g1 = a[:mid]
    g2 = a[mid:]
    merge_sort2(g1) # 재귀 호출로 첫 번째 그룹을 정렬
    merge_sort2(g2) # 재귀 호출로 두 번째 그룹을 정렬
    # 두 그룹을 하나로 병합
    i1 = 0
    i2 = 0
    ia = 0
    while i1 < len(g1) and i2 < len(g2):
        if g1[i1] < g2[i2]:
            a[ia] = g1[i1]
            i1 +=1
            ia +=1
        else:
            a[ia] = g2[i2]
            i2 +=1
            ia +=1
        # 아직 남아 있는 자료들을 결과에 추가
    while i1<len(g1):
        a[ia] = g1[i1]
        i1 += 1
        ia += 1
    while i2 < len(g2):
        a[ia] = g2[i2]
        i2 += 1
        ia += 1

d = [6,8,3,9,10,1,2,4,7,5,2,2,2]
merge_sort2(d)
d
# 리턴 값이 없고 리스트 내부의 값을 직접 바꿈!


# 병합정렬 내림차순
def merge_sort_des(a):
    n = len(a)
    # 종료 조건 : 정렬할 리스트의 자료 개수가 한 개 이하이면 정렬할 필요 없음.
    if n <= 1:
        return a
        ## 재귀함수는 종료조건을 '반복문의 종료' 가 아니라 함수 자체에 넣어줌.
    # 그룹을 나누어 각각 병합정렬을 호출
    mid = n//2 # 중간을 기준으로 두 그룹으로 나눔
    g1 = merge_sort_des(a[:mid]) # 재귀 호출로 첫 번째 그룹 정렬
    g2 = merge_sort_des(a[mid:]) # 재귀 호출로 두 번째 그룹 정렬
    # 두 그룹을 하나로 병합
    result = [] # 두 그룹을 합쳐 만들 최종결과
    while g1 and g2: # 두 그룹에 모두 자료가 남아있는 동안 반복
        if g1[0] > g2[0]: # 두 그룹의 맨 앞 자료 값을 비교
            result.append(g1.pop(0))
        else:
            # g2의 값이 더 작으면 그 값을 빼내어 결과로 추가
            result.append(g2.pop(0))
    while g1:
        result.append(g1.pop(0))
    while g2:
        result.append(g2.pop(0))
    return result

merge_sort_des([1,9,8,7,6,5,4,3,2,2,2,2,2])




# 일반적인 병합정렬
def merge_sort2_des(a):
    n = len(a)
    # 종료 조건 : 정렬할 리스트의 자료 개수가 한 개 이하일 땐 정렬할 필요가 없음.
    if n <=1:
        return
    # 그룹을 나누어 각각 병합정렬 호출
    mid = n//2
    g1 = a[:mid]
    g2 = a[mid:]
    merge_sort2_des(g1) # 재귀 호출로 첫 번째 그룹을 정렬
    merge_sort2_des(g2) # 재귀 호출로 두 번째 그룹을 정렬
    # 두 그룹을 하나로 병합
    i1 = 0
    i2 = 0
    ia = 0
    while i1 < len(g1) and i2 < len(g2):
        if g1[i1] > g2[i2]:
            a[ia] = g1[i1]
            i1 +=1
            ia +=1
        else:
            a[ia] = g2[i2]
            i2 +=1
            ia +=1
        # 아직 남아 있는 자료들을 결과에 추가
    while i1<len(g1):
        a[ia] = g1[i1]
        i1 += 1
        ia += 1
    while i2 < len(g2):
        a[ia] = g2[i2]
        i2 += 1
        ia += 1

d = [6,8,3,9,10,1,2,4,7,5,2,2,2]
merge_sort2_des(d)
d