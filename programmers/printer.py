priorities = [1, 1, 9, 1, 1, 1]	

def solution(priorities, location):
    answer = ''
    index_list = list(range(len(priorities)))
    done_pri = []
    done_idx = []

    while True:
        if not priorities:
            break
        if priorities[0] < max(priorities):
            priorities.append(priorities.pop(0))
            index_list.append(index_list.pop(0))
        else:
            done_pri.append(priorities.pop(0))
            done_idx.append(index_list.pop(0))
        
    return (done_idx.index(location)+1)





def solution(priorities, location):
    idxlist = list(range(len(priorities)))
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
    return (comp_idx.index(location)+1)

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
    return (comp_idx.index(location)+1)