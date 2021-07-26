import sys
from itertools import combinations

sys.stdin = open('input.txt')
q = lambda : map(int, sys.stdin.readline().split())



def success(): # Is from i, to i ?
    for i in range(1, N+1): # 모든 세로선에서 시작
        sero = i
        garo = 1
        while garo < H + 1:
            if arr[garo][sero] == 1:
                sero += 1
            elif arr[garo][sero-1] == 1:
                sero -= 1
            garo += 1

        if sero != i:
            return False

    return True


def findCadidate(): # find cadidate that can be placed sadary
    temp = []
    for r in range(1, H + 1):
        for c in range(1, N+1):
            if arr[r][c] == 0 and arr[r][c-1] == 0 and (c + 1 < N + 1 and arr[r][c+1] == 0):
                temp.append((r, c))

    return temp



def setSadary(rocations, value): # put or remove sadary
    for r, c in rocations:
        arr[r][c] = value



def solution(cadidate):

    # 사다리 0~3개 놨을 때
    for i in range(4):
        for temp in list(combinations(cadidate, i)):
            setSadary(temp, 1)
            if success():
                return i
            setSadary(temp, 0)

    return -1



N, M, H = q()
arr = [[0 for _ in range(N + 1)] for __ in range(H + 1)]
for _ in range(M):
    a, b = q()
    arr[a][b] = 1


cadidate = findCadidate()
print(solution(cadidate))
