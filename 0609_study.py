# l = [1,2,3,4,5]
# del l[0]

# l.remove(0)
# l

# dartResult = '1D2S#10S'
# dartResult = list(dartResult)
# first_round = []
# second_round = []
# third_round = []

# def number_extractor(dartResult):
#     points = []
#     for i in dartResult[:2]:
#         if i.isdigit():
#             points.append(i)
#             dartResult.remove(i)
#     points = int(''.join(points))
#     return points

# def star_hash_extractor(dartResult):
#     if dartResult[0]=='*':
#         first_round *= 2
#         del dartResult[0]
#     elif dartResult[0]=='#':
#         first_round *= -1
#         del dartResult[0]
#     else:
#         pass


# #1라운드
# for i in dartResult[:2]:
#     if i.isdigit():
#         first_round.append(i)
#         dartResult.remove(i)
# first_round = int(''.join(first_round))

# if dartResult[0]=='D':
#     first_round = first_round**2
# elif dartResult[0]=='T':
#     first_round = first_round**3
# del dartResult[0]

# # 1라운드 끝, *# 잡기
# if dartResult[0]=='*':
#     first_round *= 2
#     del dartResult[0]
# elif dartResult[0]=='#':
#     first_round *= -1
#     del dartResult[0]
# else:
#     pass

# # 2라운드
# for i in dartResult[:2]:
#     if i.isdigit():
#         second_round.append(i)
#         dartResult.remove(i)
# second_round = int(''.join(second_round))

# if dartResult[0]=='D':
#     second_round = second_round**2
# elif dartResult[0]=='T':
#     second_round = second_round**3
# del dartResult[0]

# # 2라운드 끝, *# 잡기
# if dartResult[0]=='*':
#     first_round *= 2
#     second_round *= 2
#     del dartResult[0]
# elif dartResult[0]=='#':
#     second_round *= -1
#     del dartResult[0]
# else:
#     pass

# # 3라운드
# for i in dartResult[:2]:
#     if i.isdigit():
#         third_round.append(i)
#         dartResult.remove(i)
# third_round = int(''.join(third_round))

# if dartResult[0]=='D':
#     third_round = third_round**2
# elif dartResult[0]=='T':
#     third_round = third_round**3
# del dartResult[0]

# # 3라운드 끝, *# 잡기
# try:
#     if dartResult[0]=='*':
#         second_round *= 2
#         third_round *= 2
#         del dartResult[0]
#     elif dartResult[0]=='#':
#         third_round *= -1
#         del dartResult[0]
#     else:
#         pass
# except:
#     pass

# answer = first_round +second_round+third_round
# print(answer)


# ###############


# def number_extractor(dartResult):
#     points = []
#     for i in dartResult[:2]:
#         if i.isdigit():
#             points.append(i)
#             dartResult.remove(i)
#     points = int(''.join(points))
#     return points

# def power_extractor(dartResult, Round):
#     if dartResult[0]=='D':
#         Round = Round**2
#     elif dartResult[0]=='T':
#         Round = Round**3
#     del dartResult[0]
#     return Round

# def star_hash_extractor(dartResult, now_score, before_score):
#     try:
#         if dartResult[0]=='*':
#             before_score *= 2
#             now_score *= 2
#             del dartResult[0]
#         elif dartResult[0]=='#':
#             now_score *= -1
#             del dartResult[0]
#         else:
#             pass
#     except:
#         pass
#     return now_score, before_score

# def solution(dartResult):
#     dartResult = list(dartResult)

#     #1라운드
#     first_round = number_extractor(dartResult)
#     first_round = power_extractor(dartResult, first_round)
#     # 1라운드 끝, *# 잡기
#     first_round = star_hash_extractor(dartResult, first_round, 0)[0]

#     # 2라운드
#     second_round = number_extractor(dartResult)
#     second_round = power_extractor(dartResult, second_round)
#     # 2라운드 끝, *# 잡기
#     second_round, first_round = star_hash_extractor(dartResult, second_round, first_round)

#     # 3라운드
#     third_round = number_extractor(dartResult)
#     third_round = power_extractor(dartResult, third_round)
#     # 3라운드 끝, *# 잡기
#     third_round, second_round = star_hash_extractor(dartResult, third_round, second_round)

#     answer = first_round +second_round+third_round
#     return answer



# #################
# #################
# #################
# def solution(dartResult):
#     dartResult = list(dartResult)
#     first_round = []
#     second_round = []
#     third_round = []

#     #1라운드
#     for i in dartResult[:2]:
#         if i.isdigit():
#             first_round.append(i)
#             dartResult.remove(i)
#     first_round = int(''.join(first_round))

#     if dartResult[0]=='D':
#         first_round = first_round**2
#     elif dartResult[0]=='T':
#         first_round = first_round**3
#     del dartResult[0]

#     # 1라운드 끝, *# 잡기
#     if dartResult[0]=='*':
#         first_round *= 2
#         del dartResult[0]
#     elif dartResult[0]=='#':
#         first_round *= -1
#         del dartResult[0]
#     else:
#         pass

#     # 2라운드
#     for i in dartResult[:2]:
#         if i.isdigit():
#             second_round.append(i)
#             dartResult.remove(i)
#     second_round = int(''.join(second_round))

#     if dartResult[0]=='D':
#         second_round = second_round**2
#     elif dartResult[0]=='T':
#         second_round = second_round**3
#     del dartResult[0]

#     # 2라운드 끝, *# 잡기
#     if dartResult[0]=='*':
#         first_round *= 2
#         second_round *= 2
#         del dartResult[0]
#     elif dartResult[0]=='#':
#         second_round *= -1
#         del dartResult[0]
#     else:
#         pass

#     # 3라운드
#     for i in dartResult[:2]:
#         if i.isdigit():
#             third_round.append(i)
#             dartResult.remove(i)
#     third_round = int(''.join(third_round))

#     if dartResult[0]=='D':
#         third_round = third_round**2
#     elif dartResult[0]=='T':
#         third_round = third_round**3
#     del dartResult[0]

#     # 3라운드 끝, *# 잡기
#     try:
#         if dartResult[0]=='*':
#             second_round *= 2
#             third_round *= 2
#             del dartResult[0]
#         elif dartResult[0]=='#':
#             third_round *= -1
#             del dartResult[0]
#         else:
#             pass
#     except:
#         pass

#     answer = first_round +second_round+third_round
#     return answer





l = [1,2,3,4,5]

for i in l:
    print(i)
    if i==3:
        print('this')
    else:
        pass

print('done')