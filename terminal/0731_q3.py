from mmap import MAP_ANON
import sys 
import pandas as pd
sys.stdin = open('/Users/heechankang/Downloads/drive-download-20210731T001519Z-001/3번파리퇴치/input.txt', 'r')


T = int(input())
for t in range(1, T+1):
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

    print('#%d %d'%(t, max(temp)))


########

import sys 
import pandas as pd
sys.stdin = open('/Users/heechankang/Downloads/drive-download-20210731T001519Z-001/3번파리퇴치/input.txt', 'r')


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    # N개 행렬 만들기
    MAP = [list(map(int, input().split())) for  _ in range(N)]
    max_sum = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            sumij = 0
            for deep_i in range(i, i+M):
                for deep_j in range(j, j+M):
                    sumij += MAP[deep_i][deep_j]
            if max_sum< sumij:
                

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

    print('#%d %d'%(t, max(temp)))


