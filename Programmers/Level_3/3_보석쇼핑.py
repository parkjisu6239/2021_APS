# def solution(gems):
#     answer = []
#     distinct_gems = set(gems)
#     gems_cnt = len(distinct_gems)
#
#     # 시작 인덱스
#     for i in range(len(gems) - gems_cnt + 1):
#         # 어디까지 확인할건지
#         for j in range(gems_cnt, len(gems) - i + 1):
#             if set(gems[i: i+j]) == distinct_gems:
#                 if not answer:
#                     answer = [i+1, i+j]
#                 else:
#                     if j-1 < answer[1] - answer[0]:
#                         answer = [i + 1, i + j]
#
#     return answer
#
#
# print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
# print(solution(["AA", "AB", "AC", "AA", "AC"]))
# print(solution(["XYZ", "XYZ", "XYZ"]))



def solution(gems):
    start = 1
    end = 1
    start_idx = 0
    end_idx = len(gems)-1
    while start or end:
        if gems[end_idx] in gems[:end_idx]:
            end_idx -= 1
        else:
            end = 0

        if end == 0:
            if gems[start_idx] in gems[start_idx+1:]:
                start_idx += 1
            else:
                start = 0


    return [start_idx+1, end_idx+1]


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))