def solution(strings, n):
    answer = []
    
    return answer


strings = ["sun", "bed", "car"]
n = 1
strings = ["abce", "abcd", "cdx"]	
n = 2
answer = []

temp = [str for str in strings if str[2]=='c']
temp



for i in range(ord('a'), ord('z')+1):
    temp = []
    temp.append([str if str[n]==i in strings])
    print(temp)


strings = ["sun", "bed", "car"]
n = 1
#strings = ["abce", "abcd", "cdx"]	
#n = 2
answer = []
temp = []
for i in strings:
    i = i[n:] + i[:n]
    temp.append(i)
temp = sorted(temp)
for j  in temp:
    j = j[-n:]+j[:-n]
    answer.append(j)
print(answer)




strings = ["sun", "bed", "car"]
n = 1
strings = ["abce", "abcd", "cdx"]	
n = 2
answer = []
strings.sort()
for i in range(ord('a'), ord('z')+1):
    for j in strings:
        if ord(j[n])==i:
            answer.append(j)
print(answer)


strings = ["sun", "bed", "car"]
n = 1
strings = ["abce", "abcd", "cdx"]	
n = 2
print(sorted(sorted(strings), key = lambda x: x[n]))
print(sorted(strings, key = lambda x: x[n]))



def solution(strings, n):
    answer = []
    strings.sort()
    for i in range(ord('a'), ord('z')+1):
        for j in strings:
            if ord(j[n])==i:
                answer.append(j)
    return answer