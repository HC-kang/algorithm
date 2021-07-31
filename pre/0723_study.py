# 재귀 예시
def milkis(n, k):
    print('응애')
    if n ==k:
        print(f'{k}번째 return')
        return
    else:
        print(k)
        milkis(n, k+1)
        print(f'{k}돌아온다.')
milkis(3, 0)


def coke(n, k):
    print('시작')
    if n==k:
        print('종료조건')
        return
    else:
        print(f'{k}번째 재귀 실행')
        coke(n, k+1)
        print(f'{k}번째 재귀 종료')
coke(3,1)

# 재귀 삼각
def triangle_number(n):
    if n<=0:
        return 0
    else:
        print(n+triangle_number(n-1))
        return n + triangle_number(n-1)

triangle_number(3)


for i in range(1, 11):
    print(f'{i}까지의 합: {triangle_number(i)}')


# 재귀 삼각+
def tri_num(n):
    





######################################


data = [7,4,1,0,0,6,0,7,0]

# for i in data:
#     print()
#     for j in range(i):
#         print([0], end = '')


import numpy as np

cnt = len(data)
target_index = np.argmax(data)
res = 0

for i in range(target_index+1, cnt):
    if data[target_index] == data[i]:
        res += 1
print(cnt - target_index - res - 1)



#################################

route = [1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7]

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

#############################
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000

cnt = int(input())
for i in range(cnt):
    
