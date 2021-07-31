import sys 
import numpy as np
sys.stdin = open('/Users/heechankang/projects/pythonworkspace/git_study/algorithm question/8번 사다리/input.txt', 'r')

T = 10
for t in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for  _ in range(100)]
    # 시작점
    endpoint = 99, np.argmax(MAP[-1])
    # 현위치
    y, x = endpoint
    while True:
        if y==0:
            break
        if x==99:
            if MAP[y][x-1]==1:
                while MAP[y][x-1]==1:
                    x -=1
                    if x==0: break
                    # print(f"x, y:", x, y)
                y-=1
            else:
                y -= 1
        elif x==0:
            if MAP[y][x+1]==1:
                while MAP[y][x+1]==1:
                    x +=1
                    if x==99: break
                    # print(f"x, y:", x, y)
                y-=1
            else:
                y -= 1
        elif 0<x<99:
            if MAP[y][x-1]==1:
                while MAP[y][x-1]==1:
                    x -=1
                    if x==0: break
                    # print(f"x, y:", x, y)
                y-=1
            elif MAP[y][x+1]==1:
                while MAP[y][x+1]==1:
                    x +=1
                    if x==99: break
                    # print(f"x, y:?", x, y)
                y-=1
            else:
                y -= 1
                # print(f"x, y:", x, y)

    print(f'#{t} {x}')


