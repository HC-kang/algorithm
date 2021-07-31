s="aabbaccc"	
s="ababcdcdababcdcd"	
s="abcabcdede"	
s="abcabcabcabcdededededede"	
s="xababcdcdababcdcd"


def solution(s):
    answer = []
    _s = []
    for i in range(1, len(s)+1):
        _s.append([])
        for j in range(0, len(s), i):
            _s[i-1].append(s[j:j+i])
    # print(_s)
    cnt = 1
    for i in range(1, len(_s[0])):
        # print(_s[0][i])
        if _s[0][i-1] ==_s[0][i]:
            cnt+=1
            print('같음', cnt, _s[0][i])
        else:
            answer.append(str(cnt))
            answer.append(_s[0][i])
            cnt = 1
            print('다름', cnt, _s[0][i])


    return ''.join(answer)

solution(s)

answer = []
for i in range(10):
    answer.append(i)
    print(answer)
answer = ''.join(answer)
print(str(answer))