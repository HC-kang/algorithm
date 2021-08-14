# inputs
'''
3
ABCCB
NNNASBBSNV
UKJWHGGHNFTCRRCTWLALX
'''
# outputs
#1 1
#2 4
#3 11


import sys 
sys.stdin = open('/Users/heechankang/projects/pythonworkspace/git_study/algorithm question/0814/0번/sample_input.txt', 'r')


T = int(input())
for t in range(1, T+1):
    S = input()

    def former(string):
        answer = ''
        while True:
            for i in range(1, len(string)):
                if string[i] != string[i-1]:
                    answer += string[i]
                if string[-1] != string[-2]:
                    answer += string[-1]
            if answer == string:
                break
            string = answer
        return answer

    a = 'ABCCB'
    former(a)
    


    print(f'#{t} {former(S)}')

    

answer
string = 'ABCCB'
string
answer
lenstring

while True:
    answer = ''
    lenstring = len(string)
    string = list(string)
    first = ''
    second = ''
    while string:
        answer, string
        first = second
        second = string.pop(0)
        first, second
        if first == second:
            first = ''
            second = ''
        answer += first
        if not string:
            answer+= second
    # if answer == string:
        # break
    string = answer
    

