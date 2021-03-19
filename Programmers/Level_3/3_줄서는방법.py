################################################
# 1. 순열 직접 생성 처음부터 탐색
def solution(n, k):
    # 순열의 k번째 값을 구하면 되는 문제? > 시간초과
    answer = []
    people = list(range(1, n + 1))
    sel = [0] * n
    visit = [0] * n

    def perm(idx):
        if idx == n:
            answer.append(list(sel))
            return

        if len(answer) == k:
            return

        for i in range(n):
            if visit[i] == 0:
                visit[i] = 1
                sel[idx] = people[i]
                perm(idx + 1)
                visit[i] = 0

    perm(0)

    return answer[k-1]


################################################
# 2. 순열 라이브러리 처음부터 탐색
from itertools import permutations
def solution1(n, k):
    # 순열의 k번째 값을 구하면 되는 문제? > 시간초과

    all = list(permutations(range(1, n+1), n))

    return list(all[k-1])


#print(solution1(3, 5))

################################################
# 1. 순열 직접 생성 맨앞은 고정하고 탐색

def factorial(n):
    if n < 2:
        return n
    else:
        return n * factorial(n - 1)


def solution2(n, k):
    # k번째를 구하는 거라서, 처음부터 구할 필요가 없음!
    # 첫번째 원소를 고정했을때, 남은 수들로 만들어지는 경우의 수는 (n-1)!
    facto = factorial(n - 1)

    # 맨앞숫자가 fix는 지나감
    fix = k // facto

    # 맨앞숫자는 fix + 1하고 하면 되고, 구해진 숫자 중에서 k - fix * facto 번째 순열을 찾으면 된다.

    answer = []
    people = list(range(1, n + 1))
    sel = [0] * n
    sel[0] = fix + 1
    visit = [0] * n
    visit[fix] = 1

    def perm(idx):
        if idx == n:
            answer.append(list(sel))
            return

        if len(answer) == k:
            return

        for i in range(n):
            if visit[i] == 0:
                visit[i] = 1
                sel[idx] = people[i]
                perm(idx + 1)
                visit[i] = 0

    perm(1)

    return answer[k - fix * facto - 1]

print(solution2(3, 5))

