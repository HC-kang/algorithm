scores = [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]




def solution(scores):
    answer = ''

    scores_t = [[0 for i in range(len(scores))] for i in range(len(scores))]
    for i in range(len(scores)):
        for j in range(len(scores)):
            scores_t[j][i] = scores[i][j]
    
    hoobo = []
    means = []
    for i in range(len(scores)):
        hoobo.append(scores[i][i])

    for j in range(len(hoobo)):
        if hoobo[j] in [max(scores_t[j]), min(scores_t[j])]:
            # 여기가 최대 최소값임.
            # print(f'{hoobo[j]}는 최대 혹은 최솟값임.')
            if scores_t[j].count(hoobo[j]) == 1:
                # 유일한 값임 -> 빼고 계산
                # print(f'{hoobo[j]}는 그중에 유일값임.')
                means.append((sum(scores_t[j])-hoobo[j]) / (len(scores)-1))
            else:
                # 중복임 -> 포함 계산
                # print(f'{hoobo[j]}는 최대최소인데 중복됨.')
                means.append(sum(scores_t[j]) / len(scores))
        else:
            # 최대 최소 아님 -> 포함계산
            # print(f'{hoobo[j]}는 중복됨.')
            means.append(sum(scores_t[j]) / len(scores))
    
    for k in means:
        if k>=90:
            answer+='A'
        elif k>=80:
            answer +='B'
        elif k>=70:
            answer +='C'
        elif k>=50:
            answer +='D'
        else:
            answer +='F'


    return answer


# 1. 각 행별 본인점수 확인

# 2. 찾은 값이 최고점?
# 2-1. 유일함? -> 빼고 계산
#       아니면 -> 포함 계산

# 3. 찾은 값이 최저점?
# 3-1. 유일? -> 빼고
#       아님? -> 포함계산

# 4. 둘다 아님? -> 포함계산

# 5. 결과에 따라 Str으로 변환

lista = [1,2,3,3,4]
lista.count(3)
sum(lista)

(sum(scores[j])-hoobo[j]) / (len(scores[j])-1)

answer = ''
answer = answer + 'a'
answer 