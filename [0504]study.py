ord('a') #97
ord('z') #122
ord('A') #65
ord('Z') #90
ord(' ') #32
ord('K') #75
ord('e') #101
ord('a') #97
ord('{') #123

chr(115)
chr(32)
chr(32)
chr(32)

def solution(s, n):
    ord_list = []
    answer = []
    for char in list(s):
        if char == " ":
            ord_list.append(ord(char))
        else:
            ord_list.append(ord(char)+n)
    for i in ord_list:
        if (90 < i <115) or (122 < i < 147):
            answer.append(chr(i-25))
        else:
            answer.append(chr(i))
    answer = ''.join(answer)
    return answer

solution('AB', 25)


def solution(s, n):
    ord_list = []
    answer = []
    for char in list(s):
        if char == " ":
            ord_list.append(ord(char))
        elif (97 <= ord(char) <=122):
            if 122 < ord(char):
                ord_list.append(ord(char)+n-26)
            else:
                ord_list.append(ord(char)+n)
        elif (65<= ord(char) <= 90):
            if 90 < ord(char):
                ord_list.append(ord(char)+n-26)
            else:
                ord_list.append(ord(char)+n)
    for i in ord_list:
        answer.append(chr(i))
    return ''.join(answer)


#####################