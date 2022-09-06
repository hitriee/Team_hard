#programmers skill check level 1
#1 더 빠름
# def solution(absolutes, signs):
#     answer = 0
#     length = len(signs)
#     for i in range(length):
#         if signs[i]:
#             answer += absolutes[i]
#         else:
#             answer -= absolutes[i]
#     return answer
#
# #1 새로운 시도 - 더 느림
# def solution(absolutes, signs):
#     answer = 0
#     length = len(signs)
#     for i in range(length):
#         answer -= absolutes[i] * (-1) ** (signs[i])
#     return answer
#
# #2 시간이 제각각
# def solution(id_list, report, k):
#     length = len(id_list)
#     write = {id_list[i]: set() for i in range(length)}
#     # 신고 받은 사람 : 신고한 사람 목록
#     for info in report:
#         user, warn = info.split()
#         write[warn].add(user)
#     # 정지된 사람 목록
#     result = []
#     for warn in id_list:
#         if len(write[warn]) >= k:
#             result.append(warn)
#
#     answer = [0] * length
#     for i in range(length):
#         user = id_list[i]
#         for warn in result:
#             if user in write[warn]:
#                 answer[i] += 1
#
#     return answer

#2
# def solution(id_list, report, k):
#     length = len(id_list)
#     write = {id_list[i]:set() for i in range(length)}
#     result = {id_list[i]:set() for i in range(length)}
#     # 신고한 사람 : 신고받은 사람 목록
#     # 신고 받은 사람 : 신고한 사람
#     for info in report:
#         user, warn = info.split()
#         write[user].add(warn)
#         result[warn].add(user)
#     # 정지된 사람 목록
#     out = set()
#     for warn in id_list:
#         if len(result[warn]) >= k:
#             out.add(warn)
#     answer = [0] * length
#     for i in range(length):
#         answer[i] = len(write[id_list[i]] & out)
#     return answer
# print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))