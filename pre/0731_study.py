# 입력
'''
3
5
477162 658880 751280 927930 297191
5
565469 851600 460874 148692 111090
10
784386 279993 982220 996285 614710 992232 195265 359810 919192 158175'''

# 출력
#1 630739
#2 740510
#3 838110

ai = []
T = int(input())
for i in range(T):
    N = int(input())
    ai.append(input().split())

answer = []

for j in ai:
    answer.append([])
    for i in j:
        temp = list(i)
        temp = [int(x) for x in temp]
        Max = max(temp)
        Min = min(temp)
        answer[-1].append(Max-Min)
print(answer)


for i in range(len(answer)):
    print('#'+str(i+1),end=' ')
    for j in answer[i]:
        print(j, end='')
    print()

######################

ai = []
T = int(input())
for i in range(T):
    N = int(input())
    ai.append(input().split())

temp = []
for i in ai:
    temp.append([int(x) for x in i])

answer = []
for i in temp:
    Max = max(i)
    
    Min = min(i)
    answer.append((Max-Min))

for i in range(len(answer)):
    print('#'+str(i+1),end=' ')
    print(answer[i])


############################
# 강사님 풀이


import sys 
sys.stdin = open('./sample_input.txt', 'r')

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    datalist= list(map(int, input().split())
    min_val =9999999
    max_val = 0
    for n in datalist
        if min > n
            min = N
        if max < n:
            max_val = n
    
    print('#%d %d'%(tc, 1)


############################


'''
3
XYPV
EOGGXYPVSY

STJJ
HOFSTJPVPP

ZYJZXZTIBSDG
TTXGZYJZXZTIBSDGWQLW
'''

#1 1
#2 0
#3 1

T = int(input())
listA = []
listB = []
for i in range(T):
    temp1 = input()
    temp2 = input()
    listA.append(temp1)
    listB.append(temp2)

listA
listB

for i in range(len(listA)):
    print('#'+str(i+1),end=' ')
    print(1 if (listA[i] in listB[i]) else 0)

##################################################

for tc in range(1, TC+1):
    str1 = input()
    str2 = input()

    if str1 in str2:
        print('#%d %d'%(tc, 1))
    else:
        print('#%d %d'%(tc, 0))

##################################################

'''
10
5 2
1 3 3 6 7
8 13 9 12 8
4 16 11 12 6
2 4 1 23 2
9 13 4 7 3
6 3
29 21 26 9 5 8
21 19 8 0 21 19
9 24 2 11 4 24
19 29 1 0 21 19
10 29 6 18 4 3
29 11 15 3 3 29
7 5
17 24 11 29 18 21 11
8 5 14 0 19 15 17
18 25 29 1 29 16 16
3 26 27 20 6 2 27
20 13 19 8 13 29 15
8 22 8 23 21 7 6
14 9 9 27 16 23 29
8 6
5 27 4 27 24 9 17 27
22 3 2 17 23 15 16 20
27 27 24 27 9 15 29 26
9 8 4 3 8 15 28 28
27 25 24 7 16 29 20 20
17 6 22 14 2 14 8 27
19 13 6 4 11 10 6 10
14 12 13 4 8 2 25 4
9 5
8 11 16 28 11 15 27 9 15
12 22 10 18 15 5 20 0 27
16 17 4 6 14 25 19 21 11
12 15 26 10 27 18 26 19 4
5 28 22 23 15 9 4 22 4
14 25 17 22 10 8 29 19 0
14 7 5 28 20 16 20 25 9
9 25 12 26 21 12 26 24 23
14 5 27 4 22 1 17 11 16
10 8
2 1 10 12 14 8 14 9 14 6
5 28 6 9 7 16 17 29 18 27
4 3 6 29 15 3 20 13 2 13
28 7 27 22 11 8 19 11 6 2
24 5 22 27 15 11 9 3 25 18
10 11 3 21 13 14 13 13 24 17
19 17 12 18 12 20 8 17 16 22
10 0 14 17 29 1 3 11 28 28
27 25 16 29 19 7 7 19 1 3
6 20 26 23 8 10 21 12 6 0
11 3
15 9 11 16 2 12 10 26 28 0 28
23 28 24 17 10 1 11 23 10 15 16
5 18 6 9 18 29 0 2 9 13 14
14 12 1 6 11 17 15 0 13 13 6
24 3 10 27 27 9 12 25 7 6 1
25 14 14 13 6 13 12 11 23 28 25
4 6 23 4 1 15 11 12 16 11 4
13 19 17 25 3 15 0 11 4 15 20
21 11 3 25 25 12 22 1 17 26 10
8 21 11 6 22 27 7 4 14 21 2
6 15 15 1 27 10 19 28 24 0 17
12 8
1 17 11 27 26 0 16 10 25 12 6 12
0 7 0 4 18 28 8 1 4 3 2 22
3 22 7 25 19 19 26 19 1 0 7 29
0 10 0 16 5 8 2 14 3 1 28 14
3 26 17 16 27 23 24 4 6 26 17 20
18 14 29 7 12 25 16 0 27 2 5 13
25 24 5 0 27 10 15 3 23 4 1 11
28 13 9 19 29 27 22 2 2 6 13 20
4 24 4 3 16 23 3 1 13 11 28 18
13 29 26 21 14 11 6 23 29 25 13 6
7 12 6 21 20 21 4 24 8 4 16 10
14 19 20 18 24 2 3 0 17 23 13 13
13 3
9 14 5 19 19 28 26 17 7 23 1 17 19
1 22 3 22 20 25 21 1 18 18 0 7 0
25 2 22 24 25 18 25 29 19 7 25 27 29
2 14 23 15 4 25 16 29 29 0 22 13 29
10 11 1 18 13 23 7 10 14 29 2 10 4
15 5 12 29 25 25 2 20 12 29 25 12 9
21 19 3 16 6 27 24 25 29 7 5 4 26
29 28 6 18 18 16 26 13 13 23 16 9 4
2 20 13 23 19 12 22 27 26 12 21 29 2
21 0 7 29 25 6 24 27 27 19 3 28 6
7 15 8 13 19 5 29 11 16 12 25 3 17
4 27 3 28 0 24 3 28 13 18 24 6 22
24 6 20 8 2 7 29 13 3 20 29 0 23
14 9
19 27 28 26 4 28 23 14 7 9 27 27 17 21
7 12 29 19 10 5 17 18 19 15 13 13 1 9
2 0 14 7 22 8 8 20 7 10 7 23 19 21
6 5 8 6 24 27 9 17 19 24 25 17 0 19
18 8 18 26 8 24 8 11 15 18 0 23 26 7
17 7 12 15 1 27 24 24 7 24 2 1 19 10
6 18 2 15 21 5 24 11 11 17 24 28 0 6
3 8 12 6 23 6 2 3 7 9 6 18 21 25
14 3 27 11 0 21 27 27 3 29 28 28 6 4
20 3 15 14 13 28 6 4 2 2 14 22 16 7
10 17 1 5 26 22 18 17 8 19 11 3 20 5
11 13 15 14 22 2 25 13 29 5 14 4 27 17
15 10 9 18 0 16 4 25 17 1 6 12 6 20
24 1 24 2 12 7 3 21 10 21 19 29 0 5
'''

#1 49
#2 159
#3 428
#4 620
#5 479
#6 941
#7 171
#8 968
#9 209
#10 1242


10
5 2
1 3 3 6 7
8 13 9 12 8
4 16 11 12 6
2 4 1 23 2
9 13 4 7 3

import sys 
sys.stdin = open('./sample_input.txt', 'r')

import pandas as pd

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    # N개 행렬 만들기
    mapping = []
    for n in range(N):
        temp=list(map(int, input().split()))
        mapping.append(temp)

df = pd.DataFrame(mapping)

temp = []
for x in range(N-M+1):
    for y in range(N-M+1):
        smallmap = df.iloc[y:y+M, x:x+M]
        # print(x, y, smallmap.sum().sum())
        temp.append(smallmap.sum().sum())

print(max(temp))