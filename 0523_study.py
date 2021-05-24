skipped = []

skipped.append(2)

skipped

if skipped:
    print(f'WarningCount: {len(skipped)}, store_id_list:{skipped}')

    



a, b = map(int, input().split())
print(a)
print(b)


a = input()

for i in range(3):
    print(a[2*i:2*i+2], end=' ')


a = float(input())
print(round(a, 2))

a, b = map(float, input().split())
print(round(a/b, 3))


a, b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(format(a/b, '.2f'))