'''
phone_book = ["119", "97674223", "1195524421"]
false
phone_book = ["123","456","789"]	
true
phone_book = ["12","123","1235","567","88"]	
false
'''

def solution(phone_book):
    answer = True
    # 번호를 하나씩 나누면?
    # 1번대
    # True 
    # 1. 맨 앞 숫자가 다 다른 경우
    # 
    # False 
    # 1. 한두자리수 번호가 있는 경우 - 대체로.. 
    # 2.  
    for i in range(len(phone_book)):
        for j in range(i+1, len(phone_book)):
            if phone_book[i] in phone_book[j]:
                print(phone_book[i], phone_book[j])
                return False
    return answer

solution(phone_book)



def solution(phone_book):
    answer = True
    lists = []
    
    for i in range(10):
        lists.append([])
    
    for i in phone_book:
        lists[int(i[0])].append(i)

    for i in lists:
        for j in range(len(i)):
            for k in range(j+1, len(i)):
                if i[j] in i[k]:
                    print(i[j], i[k])
                    return False
            for k in range(j):
                if i[j] in i[k]:
                    print(i[j], i[k])
                    return False
    return answer



solution(phone_book)




def solution(phone_book):
    answer = True
    lists = []
    
    for i in range(10):
        lists.append([])
    
    for i in phone_book:
        lists[int(i[0])].append(i)

    for i in lists:
        for j in range(len(i)):
            for k in range(j+1, len(i)):
                if i[j] in i[k]:
                    print(i[j], i[k])
                    return False
            for k in range(j):
                if i[j] in i[k]:
                    print(i[j], i[k])
                    return False
    return answer
