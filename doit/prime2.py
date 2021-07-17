counter = 0
ptr = 0
prime = [None]*500

prime[ptr] = 2
ptr += 1

for n in range(3, 1001, 2):
    for i in range(1, ptr):
        counter += 1
        if n % prime[i] == 0:
            break
    else:
        prime[ptr] = n
        ptr+=1

for i in range(ptr):
    print(prime[i])
print(f'나눗셈을 시행한 횟수: {counter}')