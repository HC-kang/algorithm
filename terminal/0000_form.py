import sys 
sys.stdin = open('/Users/heechankang/projects/pythonworkspace/git_study/algorithm/terminal/5번 농작물/input.txt', 'r')


T = 10
for t in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for  _ in range(N)]
    answer = 0


    print(f'#{t} {answer}')