print('세 정수의 최댓값 구하기')
a = int(input('정수 a'))
b = int(input('정수 b'))
c = int(input('정수 c'))

maximum = a
if b >= maximum: maximum = b;
if c >= maximum: maximum = c;

print(f'최댓값은 {maximum}')