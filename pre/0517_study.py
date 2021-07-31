#  피보나치 F(n)을 1234567로 나눈 수를 return

def solution(n):
    if n == 0 or n == 1 or n == 2:
        return 1
    else:
        return solution(n-2) + solution(n-1)

solution(0)
solution(1)
solution(2)
solution(3)
solution(4)
solution(5)
solution(6)
solution(7)

solution(36)

#####
dic = {0:1, 1:1, 2:1}
def solution(n):
    global dic
    if n in list(dic.keys()):
        return dic[n] % 1234567
    else:
        answer = solution(n-2) + solution(n-1)
        dic[n] = answer
        return answer % 1234567

solution(0)
solution(1)
solution(2)
solution(10000)




dic = {0:1, 1:1, 2:1}
dic.keys()


for i from 3 upto 5:
    print('hello')

def fib(N):
    golden_ratio = (1 + 5 ** 0.5) / 2
    return int((golden_ratio ** N + 1) / 5 ** 0.5)

fib(30)
##############################
def solution(n):
    if n<= 2:
        return 1
    first = 1
    second = 1
    for i in range(3, n+1):
        now = first + second
        second = first
        first = now
    return now
#################################
def fib(self, N: int) -> int:
    if (N <= 1):
        return N
    if (N == 2):
        return 1

    current = 0
    prev1 = 1
    prev2 = 1

    # Since range is exclusive and we want to include N, we need to put N+1.
    for i in range(3, N+1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    return current

##########################

def sol(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a

for i in range(1, 11):
    print(sol(i))