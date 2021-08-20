clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]

def solution(clothes):
    kinds = {}
    for i in clothes:    
        if i[-1] in kinds.keys():
            kinds[i[-1]] += 1
        else:
            kinds[i[-1]] = len(i)-1 

    return answer

kinds[i[-1]]

