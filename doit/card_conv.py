def card_conv(x:int, r:int) -> str:
    ''' 정숫값 x를 r 진수로 변환하여 문자열로 표현'''

    d = '' # 변환 후 문자열, 빈 문자열로 초기화
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    while x > 0:
        d += dchar[x % r]
        x//=r
    
    return d[::-1]


if __name__ == '__main__':
    print('10진수를 n진수로 변환')

    while True:
        while True:
            no = int(input('변환할 값으로 음이 아닌 정수를 입력: '))
            if no > 0:
                break
        
        while True:
            cd = int(input('어떤 진수로 변경? :'))
            if 2 <= cd <= 36:
                break
        
        print(f'{cd}진수로는 {card_conv(no, cd)}입니다.')

        retry = input('한번 더? (Y/n)')
        if retry in ['N', 'n']:
            break