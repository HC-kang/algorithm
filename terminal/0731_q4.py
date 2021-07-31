'''
3
2
2 2 4 4 1
3 3 6 6 2
3
1 2 3 3 1
3 6 6 8 1
2 3 5 6 2
3
1 4 8 5 1
1 8 3 9 1
3 2 5 8 2
'''

#1 4
#2 5
#3 7

import sys 
import pandas as pd
sys.stdin = open('/Users/heechankang/projects/pythonworkspace/git_study/algorithm/terminal/4번 색칠하기/sample_input.txt', 'r')


T = int(input())
for t in range(1, T+1):
    mapping = []
    for i in range(10):
        mapping.append([])
        for j in range(10):
            mapping[-1].append(0)
    df = pd.DataFrame(mapping)

    N = int(input())
    for n in range(N):
        temp = list(map(int, input().split()))
        df.iloc[temp[0]:temp[2]+1, temp[1]:temp[3]+1] += temp[4]
    mapping = df.values.tolist()
    cnt = 0
    for i in mapping:
        for j in i:
            if j==3:
                cnt+=1


    print('#%d %d'%(t, cnt))
