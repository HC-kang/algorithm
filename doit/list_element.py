x = [15, 64, 7, 3.14, [32, 55], 'ABC']
for i in range(len(x)):
    print(f'x[{i}] = {x[i]}')

x = [[1,2,3], [4,5,6]]
y = x.copy()
x[0][1] = 9
y

import copy
x = [[1,2,3], [4,5,6]]
y = copy.deepcopy(x)
x[0][1] = 9
y