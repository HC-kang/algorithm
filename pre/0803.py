record = ["Enter uid1234 Muzi", 
          "Enter uid4567 Prodo",
          "Leave uid1234",
          "Enter uid1234 Prodo",
          "Change uid4567 Ryan"]

# answer  ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]


def solution(record):
    answer = []
    an = {}
    for i in record:
        if i.split()[0] == 'Enter' or i.split()[0] == 'Change':
            an[i.split()[1]] = i.split()[2]
        elif i.split()[0] == 'Leave':
            # del(an[i.split()[1]])
            pass

    for i in record:
        if i.split()[0]=='Enter':
            answer.append(f'{an[i.split()[1]]}님이 들어왔습니다.')
        elif i.split()[0]=='Leave':
            answer.append(f'{an[i.split()[1]]}님이 나갔습니다.')

    return answer

solution(record)



def solution(record):
    answer = []
    re = []
    an = []
    for i in record:
        # 엔터
        if i.split()[0] == 'Enter':
            if i.split()[1] not in an:
                re.append((i.split()[1], i.split()[2]))
                an.append(i.split()[1])
                answer.append(i.split()[2]+'님이 들어왔습니다.')
            else:
                for j in range(len(an)):
                    if an[j]==i.split()[1]:
                        answer[i] = 

        # 리브
        elif i.split()[0] == 'Leave':
            an.append(i.split()[1])
            answer.append(re[re[0].index(i.split()[1])][1]+'님이 나갔습니다.')
            re.pop(re[0].index(i.split()[1]))



    re
    answer
    an
    return answer