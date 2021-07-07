x = ['John', 'George', 'Paul', 'Ringo']

for i, j in enumerate(x):
    print(f'x[{i+1}]: {j}')


x = ['John', 'George', 'Paul', 'Ringo']
for i, j in enumerate(x, 1):
    print(f'x[{i}]: {j}')