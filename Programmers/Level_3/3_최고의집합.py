from itertools import combinations_with_replacement
def solution(n, s):
    answer = list(combinations_with_replacement(range(1, s+1), n))

    good_answer = []
    max_multi = 0
    for i in range(len(answer)):
        if answer[i][0] * answer[i][1] > max_multi and sum(answer[i]) == s:
            max_multi = answer[i][0] * answer[i][1]
            good_answer = answer[i]

    if good_answer:
        return good_answer
    else:
        return [-1]

print(solution(2, 8))