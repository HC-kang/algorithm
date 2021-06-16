lottos = [44, 1, 0, 0, 31, 25]	
win_nums = [31, 10, 45, 1, 6, 19]	

lottos = [0, 0, 0, 0, 0, 0]	
win_nums = [38, 19, 20, 40, 15, 25]	

lottos = [1, 5, 6, 10, 7, 2]	
win_nums = [20, 9, 3, 45, 4, 35]	

def solution(lottos, win_nums):
    l_n = len(list(set(lottos)-set(win_nums)-{0})) # 무조건 틀린 수
    ln = len(list(set(lottos)&set(win_nums))) # 무조건 맞는 수
    return [min(6,1+l_n), min(6,7-ln)]


def solution(lottos, win_nums):
    return [min(6,1+len(list(set(lottos)-set(win_nums)-{0}))), min(6,7-len(list(set(lottos)&set(win_nums))))]

solution(lottos, win_nums)

a = {0,1,2,3}
a -{0}


a, b = map(int, input().split())
a = 20
b = 23
num = ''
for i in range(1, a):
    num += str(i)
    print(num)
    if len(num)>=b:
        num = num[b:b+1]
        break
print(int(num))

1~9 9 9
10~99 89 89*2=178
100~999 899  899*3 = 2697

(10-1)**1
100


#############

a, b = map(int, input().split())
a = 20
b = 190
num = ''
k=1
i=1
index=1
b=180
while True:
    if k<=b:
        if k>b:
            break
        k+=(9*10**(i-1))*i
        i+=1
    else: break
print(i) # b가 속한 구역은 i-1자릿수
print(k)


b-=(9*10**(i-3))*(i-2)
if b%(i-1)
b=b//(i-1)
b

i


for i in range(1, 10):
    print((9*10**(i-1)-1)*i)