def solution(priorities, location):
    idxlist = list(range(len(priorities)))
    idxlist

    comp_pri = []
    comp_idx = []

    while True:    
        if not priorities:
            break
        if priorities[0] < max(priorities):
            priorities.append(priorities.pop(0))
            idxlist.append(idxlist.pop(0))
        else:
            comp_pri.append(priorities.pop(0))
            comp_idx.append(idxlist.pop(0))
    return (comp_idx.index(locations)+1)




# 2 1 3 1 4 1
# 0 1 2 3 4 5

# 4 1 2 1 3 1
# 4 5 0 1 2 3

# 1 2 1 3 1
# 5 0 1 2 3

# 3 1 1 2 1
# 2 3 5 0 1

# 1 1 2 1
# 3 5 0 1

# 2 1 1 1
# 0 1 3 5

# 2 1 1 1
# 0 1 3 5





priorities = [2, 1, 3, 2]
location = 2


priorities = [1, 1, 9, 1, 1, 1]
location = 0




idxlist = list(range(len(priorities)))
idxlist

comp_pri = []
comp_idx = []

while True:    
    if not priorities:
        break
    if priorities[0] < max(priorities):
        priorities.append(priorities.pop(0))
        idxlist.append(idxlist.pop(0))
    else:
        comp_pri.append(priorities.pop(0))
        comp_idx.append(idxlist.pop(0))
print(comp_idx.index(locations)+1)



# 다른사람 풀이
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer

solution(priorities, location)


a = list(enumerate(priorities))
a

def solution(priorities, location):
    jobs = len(priorities)
    answer = 0
    cursor = 0
    while True:
        print('priorities[cursor%jobs]',priorities[cursor%jobs])
        print('cursor%jobs',cursor%jobs)
        print('cursor', cursor)
        print('answer', answer)
        
        if max(priorities) == priorities[cursor%jobs]:
            priorities[cursor%jobs] = 0
            answer += 1
            if cursor%jobs == location:
                break
        cursor += 1   
    return answer