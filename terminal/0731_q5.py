'''
1
5
14054
44250
02032
51204
52212
'''
#1 23


import sys 
sys.stdin = open('/Users/heechankang/projects/pythonworkspace/git_study/algorithm/terminal/5번 농작물/input.txt', 'r')


T = int(input())
for t in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, list(input()))) for  _ in range(N)]
    answer = 0

    for i in range(N//2):
        answer += sum(MAP[i][(N//2)-i:(N//2)+1+i])
        # print(sum(MAP[i][(N//2)-i:(N//2)+1+i]))
        answer += sum(MAP[(N-1)-i][(N//2)-i:(N//2)+1+i])
        # print(sum(MAP[(N-1)-i][(N//2)-i:(N//2)+1+i]))
    answer += sum(MAP[N//2])
    # print(sum(MAP[N//2]))
    # print('T:', T)
    # print('N:', N)
    # print('MAP:', MAP)

    print('#%d %d'%(t, answer))