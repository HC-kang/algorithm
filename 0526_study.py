d = []
for i in range(20):
    d.append([])
    for j in range(20):
        d[i].append(0)

a = int(input())
for i in range(a):
    x, y = map(int, input().split())
    d[x][y] = 1

for i in range(1, 20):
    for j in range(1, 20):
        print(d[i][j], end = ' ')
    print()




##############
d = []

for i in range(20):
    d.append([])
    for j in range(20):
        d[i].append(0)

a = int(input())
for i in range(a):
    x, y = map(int, input().split())
    d[y] = d[y] + 1
    for j in range(20):
        d[j][x]= 1
        
for i in range(1, 20):
    for j in range(1, 20):
        print(d[i][j], end = ' ')
    print()

##############
d = []
for i in range(19):
    lists = list(map(int, input().split()))
    d.append(lists)
    
a = int(input())

for i in range(a):
    x, y = map(int, input().split())
    for j in range(19):
        if d[y-1][j] == 0:
            d[y-1][j] = 1
        else:
            d[y-1][j] = 0
    for k in range(19):
        if d[k][x-1] == 0:
            d[k][x-1] = 1
        else:
            d[k][x-1] = 0
            
for i in range(19):
    for j in range(19):
        print(d[i][j], end = ' ')
    print()

######################

h, w = map(int, input('가로세로').split())

lists = []

for i in range(h):
    lists.append([])
    for j in range(w):
        lists[i].append(0)

n = int(input('몇회?'))

for i in range(n):
    l, d, x, y = map(int, input('길, 방, 좌표').split())
    x = x-1
    y = y-1
    print(l, d, x, y)
    for j in range(l):
        if d == 0:
            lists[x][y]=1
            y+=1
        elif d==1:
            lists[x][y]=1
            x+=1

print(lists)

#########################
h, w = map(int, input().split())

lists = []

for i in range(h):
    lists.append([])
    for j in range(w):
        lists[i].append(0)

n = int(input())

for i in range(n):
    l, d, x, y = map(int, input().split())
    x = x-1
    y = y-1
    for j in range(l):
        if d == 0:
            lists[x][y]=1
            y+=1
        elif d==1:
            lists[x][y]=1
            x+=1

for i in range(h):
    for j in range(w):
        print(lists[i][j], end = ' ')
    print()

####################
lists = []

for i in range(10):
    lists.append(list(map(int, input().split())))

x, y = 1, 1
while True:
    lists[x][y] = 9
    if lists[x][y+1]==0:
        y+=1
    elif lists[x+1][y]==0:
        x+=1
    else:
        break

for i in range(10):
    for j in range(10):
        print(lists[i][j], end = ' ')
    print()