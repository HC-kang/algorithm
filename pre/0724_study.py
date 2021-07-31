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

N, M = map(int, input().split())  # M = depth
result = []
visitied = [False]*(N+1)

def dfs(depth, N, M):
    if depth == M+1:  # 깊이까지 탐색 완료
        for i in range(0,len(result)):
            print(result[i],end=" ")
        print()
        return
    for num in range(1,N+1):
        if not visitied[num]:
            visitied[num] = True
            result.append(num)
            dfs(depth+1, N, M)
            visitied[num] = False
            result.pop()

dfs(1,N,M)

##################################

route = [1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7]

len(route)

size = max(route)
size

mapper = [(route[2*i], route[2*i+1]) for i in range(len(route)//2)]
mapper


G = [[0 for i in range(size)] for j in range(size)]
G

for (i, j) in mapper:
    G[i-1][j-1] += 1
    G[j-1][i-1] += 1
G
    
visited = [0] * size
visited

def dfs(v):
    visited[v] = 1
    print(v+1, end = '')
    for w in range(size):
        if G[v][w] == 1 and visited[w]==0:
            dfs(w)

dfs(0)
    















V, E = map(int, input().split())

temp = list(map(int, input().split()))

G = [0 for i in range(V+1) for j in range(V+1)]

visited = [0 for i in range(V+1)]
visited

G = [[0 for i in range(V+1)] for j in range(V+1)]
G

dlist = [(temp[2*i], temp[2*i+1]) for i in range(len(route)//2)]
dlist


for i, j in dlist:
    G[i-1][j-1] +=1
    G[j-1][i-1] +=1

G

def dfs(v):
    visited[v] = 1
    print(v, end=' ')
    for w in range(V+1):
        if G[v][w] == 1 and visited[w] == 0:
            dfs(w)


dfs(0)
visited

#########################

V = 7

def DFS_recur(G, v):
    visited[v] = True
    print(v, end = '')
    for i in range(1, V+1):
        if G[v][i] and not visited[i]:
            DFS_recur(G, i)

visited = [0] * (V+1)
G = [[0 for i in range(V+1)] for j in range(V+1)]

# edges = list(map(int, input().split()))
edges = [1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7]

for i in range(0, len(edges), 2):
    u = edges[i]
    v = edges[i+1]
    G[u][v] = G[v][u] = 1

DFS_recur(G, 1)


#############
# 단지 번호 붙이기

7
0110100
0110101
1110101
0000111
0100000
0111110
0111000

N = int(input())
matrix = []
for i in range(N):
    matrix.append(list(map(int, input().split())))
matrix

N = 7
matrix = [
    [0,1,1,0,1,0,0],
    [0,1,1,0,1,0,1],
    [1,1,1,0,1,0,1],
    [0,0,0,0,1,1,1],
    [0,1,0,0,0,0,0],
    [0,1,1,1,1,1,0],
    [0,1,1,1,0,0,0]
    ]
visited = [[0 for i in range(N)] for j in range(N)]
visited

    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

nums = 0
cnt = 1
numlist = []

def probe(x, y, cnt):
    visited[x][y] = True
    global nums
    if matrix[x][y] == 1:
        nums += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<N:
            if matrix[nx][ny] and not visited[nx][ny]:
                probe(nx, ny, cnt)

for a in range(N):
    for b in range(N):
        if matrix[a][b] and not visited[a][b]:
            probe(a, b, cnt)
            numlist.append(nums)
            nums = 0

print(len(numlist))
for n in sorted(numlist):
    print(n)







N = 7
matrix = [
    [0,1,1,0,1,0,0],
    [0,1,1,0,1,0,1],
    [1,1,1,0,1,0,1],
    [0,0,0,0,1,1,1],
    [0,1,0,0,0,0,0],
    [0,1,1,1,1,1,0],
    [0,1,1,1,0,0,0]
    ]

visited = [[0 for i in range(N)] for j in range(N)]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

nums = 0
cnt = 1
numlist = []

def cursor(x, y):
    visited[x][y] = True
    global nums
    if matrix[x][y]:
        nums +=1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<N:
            if matrix[nx][ny] and not visited[nx][ny]:
                cursor(nx, ny)

for a in range(N):
    for b in range(N):
        if matrix[a][b] and not visited[a][b]:
            cursor(a, b)
            numlist.append(nums)
            nums = 0

print(len(numlist))
print(numlist)


######
# BFS 기본

import collections

def bfs(v): # 출발 노드
    visited = [0] * (n+1) # 노드가 1번부터 n개 까지 인 경우에 사용
    que = collections.deque() # 하나씩 넣고 빼니까, que를 사용한다.
    que.append(v) # que에 시작점 v를 넣는다. 경우에 따라 (y, x)인 튜플 형태로 들어가기도 함.
    visited[v] = 1 # append를 하는 순간 visited 에 기록한다고 외우고 풀면 편하다

    while que: # que가 비어 있으면 while을 그만 반복한다(선암기)
        t = que.popleft()
        if # answp whrjs sjgrl
            return 답 넣기
        for w in G[t]: # 연결된 간선 탐색
            if # 제약조건 넣기
                    continue
            if visited == 0: # 방문 안한 게 있는지 확인
                que.append(w)
                visited[v] == 1
    return 0 # 0이 아니어도 됨. 조건에 맞게 넣어주기


# 가중치가 생기는 경우
def bfs(v): # 출발 노드
    visited = [0] * (n+1) # 노드가 1번부터 n개 까지 인 경우에 사용
    que = collections.deque() # 하나씩 넣고 빼니까, que를 사용한다.
    que.append(v) # que에 시작점 v를 넣는다. 경우에 따라 (y, x)인 튜플 형태로 들어가기도 함.
    visited[v] = 1 # append를 하는 순간 visited 에 기록한다고 외우고 풀면 편하다

    while que: # que가 비어 있으면 while을 그만 반복한다(선암기)
        t = que.popleft()
        if # answp whrjs sjgrl
            return 답 넣기
        for w in G[t]: # 연결된 간선 탐색
            if # 제약조건 넣기
                    continue
            if visited == 0: # 방문 안한 게 있는지 확인
                que.append(w)
                visited[v] == visited[t] + 1
    return 0 # 0이 아니어도 됨. 조건에 맞게 넣어주기

 
def bfs(y, x):
    visited = [[0] * (n+1) for _ in range(n+1)]
    que = collections.deque()
    que.append((y, x))  #큐에 튜플로 넣는다.
    visited[y][x] = 1
    dx = [1, -1, 0, 0]  #델타 탐색 
    dy = [0, 0, 1, -1]
    while que:
        p, q = que.popleft()
        if # 문제조건넣기
            return #답넣기
        for d in range(4): # 연결된 간선 탐색
            nx = dx[d] + q
            ny = dy[d] + p
            if # 제약조건 넣기
                continue
            if visited[ny][nx] == 0: # 방문 안한거 있나 확인 + 조건
                que.append((ny, nx))
                visited[ny][nx] = visited[p][q] + 1

N = 7
route = [1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7]

G = [[0 for i in range(N+1)] for j in range(N+1)]
visited = [0] * (N+1)

temp = [(route[i], route[i+1]) for i in range(0, len(route), 2)]

for i, j in temp:
    G[i][j] = G[j][i] = 1

def dfs(v):
    visited[v] = 1
    print(v, end=' ')
    for i in range(V+1):
        if G[v][i] == 1 and visited[i]==0:
            dfs(i)
dfs(1)



G

def dfs(v):
    visited[v] = 1
    print(v, end=' ')
    for w in range(V+1):
        if G[v][w] == 1 and visited[w] == 0:
            dfs(w)


dfs(0)