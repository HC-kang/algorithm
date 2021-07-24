# 1,2,3,4
# 1,2,3,4

# m, n = map(int, input().split())

# lists = list(range(1, m+1))
# lists
# answers = []
# answer = ''
# start = 0
# cursor = 0
# while True:
#     if len(answers) >=3:
#         break
#     for i in range(n):
#         answer += str(lists[cursor])
#         cursor +=1

#     answers.append(answer)

# answers


n,m = list(map(int,input().split()))

 
s = []
 
def dfs():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(1,n+1):
        if i not in s:
            s.append(i)
            print(s)
            dfs()
            s.pop()
 
dfs()