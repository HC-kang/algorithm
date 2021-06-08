a = list(range(10))

print(a)


b = [i for i in range(10) if i%2==0]
b

c = [[0]*3 for _ in range(10)]
c[2][2] = 1
c

d = [[0]*4]*6
d
d[2][2]=1

e = [[1,2,3]]*5
e
e[3][1] = 1000

f = [[0]] * 20
f
f[2][0] = 1

for _ in range(10):
    print(_)

a = {1,2,3}
b = {3,4,5}
a
b
a | b