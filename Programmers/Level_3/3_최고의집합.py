# 부분집합 > 시간초과
# from itertools import combinations_with_replacement
# def solution(n, s):
#     answer = list(combinations_with_replacement(range(1, s+1), n))
#
#     good_answer = []
#     max_multi = 0
#     for i in range(len(answer)):
#         if answer[i][0] * answer[i][1] > max_multi and sum(answer[i]) == s:
#             max_multi = answer[i][0] * answer[i][1]
#             good_answer = answer[i]
#
#     if good_answer:
#         return good_answer
#     else:
#         return [-1]
#
# print(solution(2, 8))


# 더해서 s가 되는 수들의 조합중 가장 큰 것은 그 수들이 비교적 균등하게 나누어져 있을 때?
# 3, 10 > 3, 3, 4
def solution(n, s):
    numbers = s // n
    if numbers < 2:
        return [-1]

    answer = [numbers] * n # 일단 나눠 담고
    remain = s % n # 나머지는 뒤에서부터 더하기

    i = n-1
    while remain:
        answer[i] += 1
        i -= 1
        remain -= 1

    return answer

print(solution(2, 1))

