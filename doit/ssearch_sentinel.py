from typing import Any, Sequence
import copy

def seq_search(seq : Sequence, key :Any) -> int:
    a = copy.deepcopy(seq)
    a.append(key)

    i = 0
    while True:
        if a[i] == key:
            break
        i += 1
    return -1 if i == len(seq) else i

if __name__ == '__main__':
    num = int(input('원소 수를 입력하세요.'))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]:'))

    ky = int(input('검색할 값을 입력하세요.:'))

    idx = seq_search(x, ky)

    if idx == -1:
        print('검색할 값을 갖는 원소가 존재하지 않습니다.')
    else:
        print(f'검색값은 x[{idx}]에 있습니다.')