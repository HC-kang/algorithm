'''
100
0 0 225 214 82 73 241 233 179 219 135 62 36 13 6 71 179 77 67 139 31 90 9 37 93 203 150 69 19 137 28 174 32 80 64 54 18 0 158 73 173 20 0 102 107 48 50 161 246 145 225 31 0 153 185 157 44 126 153 233 0 201 83 103 191 0 45 0 131 87 97 105 97 209 157 22 0 29 132 74 2 232 44 203 0 51 0 244 212 212 89 53 50 244 207 144 72 143 0 0 
'''


'''
0 0 3 5 2 4 9 0 6 4 0 6 0 0
'''


import sys 
sys.stdin = open('/Users/heechankang/projects/pythonworkspace/git_study/algorithm/terminal/6번 조망권문제/input.txt', 'r')


T = 10
for t in range(1, T+1):
    N = int(input())
    MAP = list(map(int, input().split()))
    answer = []

    for i in range(2, len(MAP)-2):
        st1 = MAP[i]-MAP[i-2]
        st2 = MAP[i]-MAP[i-1]
        st3 = MAP[i]-MAP[i+1]
        st4 = MAP[i]-MAP[i+2]
        temp = min([st1, st2, st3, st4])
        temp = temp if temp>=0 else 0
        answer.append(temp)
    answer = sum(answer)
    print('#%d %d'%(t, answer))