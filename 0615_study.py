year=2013
while True:
    exec('result_%s = result_%s[["date", "name", "hashtags", "tweet",]]'%(year))
    year+=1
    if year==2022: break


def solution(answers):
    answer=[]
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    a_score, b_score, c_score = 0, 0, 0
    for i in range(len(answers)):
        if a[i%len(a)] == answers[i]:
            a_score+=1
        if b[i%len(b)] == answers[i]:
            b_score+=1
        if c[i%len(c)] == answers[i]:
            c_score+=1
    answer = [-1, a_score, b_score, c_score]
    return list(filter(lambda x: answer[x] == max(answer), range(len(answer))))

list(filter(lambda x: b[x]==2, range(len(b))))



############

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]	
moves = [1,5,3,5,1,2,1,4]	


def double_check(s):
    remove_index = []
    for i in range(1, len(s)):
        if s[i]==s[i-1]:
            remove_index.append(i-1)
    return remove_index

def solution(board, moves):
    results = []
    l=[]
    answer = 0
    for i in range(len(board)):
        l.append([])
        for j in range(len(board[0])):
            l[i].append(board[i][j])

    for i in moves:
        for j in range(len(board)):
            if l[j][i-1]!=0:
                results.append(l[j][i-1])
                l[j][i-1]=0
                break

    for i in range(len(results)//2):
        for j in double_check(results):
            results.pop(j)
            results.pop(j)
            answer +=1
    return answer


    ######################3

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]	
moves = [1,5,3,5,1,2,1,4]	


def double_check(s):
    remove_index = []
    for i in range(1, len(s)):
        if s[i]==s[i-1]:
            remove_index.append(i-1)
    return remove_index

results = []
l=[]
answer = 0
for i in moves:
    for j in range(len(board)):
        if board[j][i-1]!=0:
            results.append(board[j][i-1])
            board[j][i-1]=0
            break

for i in range(len(results)//2):
    for j in double_check(results):
        results.pop(j)
        results.pop(j)
        answer +=1

#############

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]	
moves = [1,5,3,5,1,2,1,4]	

board = [[0],[0],[0],[1],[1],[1],[1],[1],]
moves = [1,1,1,1,1,1,1]	


def double_check(s):
    remove_index = []
    for i in range(1, len(s)):
        if s[i]==s[i-1]:
            remove_index.append(i-1)
            break
    return remove_index

def solution(board, moves):
    results = []
    l=[]
    answer = 0
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1]!=0:
                results.append(board[j][i-1])
                board[j][i-1]=0
                break
    print(results)
    for i in range(len(results)//2):
        for j in double_check(results):
            results = results[:j]+results[j+2:]
            answer += 2
        else:
            pass
    return answer

solution(board, moves)

################
def solution(board, moves):
    cols = list(map(lambda x: list(filter(lambda y: y > 0, x)), zip(*board)))
    cols
    a, s = 0, [0]

    for m in moves:
        if len(cols[m - 1]) > 0:
            if (d := cols[m - 1].pop(0)) == (l := s.pop()):
                a += 2
            else:
                s.extend([l, d])

    return a
len(moves)
if(a:=len(moves))==10:
    print('True')
else:
    print('false')

10==10