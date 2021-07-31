progresses = [95, 90, 95, 99, 80, 99]
speeds = [5, 9, 1, 1, 1, 1]

def pusher(progresses, speeds, answer):
    checker = 0
    for i in range(len(progresses)):
        if progresses[i] < 100:
            break
        else:
            checker+=1
    if checker !=0:
        answer.append(checker)
        return progresses[checker:], speeds[checker:]
    return progresses, speeds

def solution(progresses, speeds):
    answer = []
    while progresses:
        for i in range(len(progresses)):
            progresses[i] = progresses[i]+speeds[i]
        progresses, speeds = pusher(progresses, speeds, answer)
    return answer

solution(progresses, speeds)