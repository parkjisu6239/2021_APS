import sys
from itertools import combinations

sys.stdin = open('input.txt')
q = lambda : map(int, sys.stdin.readline().split())


def success(): # Is from i, to i ?
    diff = 0 # 시작-끝이 다른 세로선 수
    for i in range(1, N+1): # 모든 세로선에서 시작
        sero = i
        garo = 1
        while garo < H + 1:
            if arr[garo][sero] == 1:
                sero += 1
            elif arr[garo][sero-1] == 1:
                sero -= 1
            garo += 1

        if sero != i: diff += 1 # 시작-끝점 다른 경우 +1
    return diff


def findCadidate(): # find cadidate that can be placed sadary
    temp = []
    for r in range(1, H + 1):
        for c in range(1, N+1):
            if arr[r][c] == 0 and arr[r][c-1] == 0 and (c + 1 < N + 1 and arr[r][c+1] == 0):
                temp.append((r, c))
    return temp


def setSadary(rocations, value): # put or remove sadary
    if value: # 사다리를 놓을 때
        for r, c in rocations:
            if arr[r][c] == 0 and arr[r][c - 1] == 0 and (c + 1 < N + 1 and arr[r][c + 1] == 0):
                arr[r][c] = value
            else:
                return False # 하나라도 못 놓으면 False
        return True # 다 놓을 수 있으면 True
    else:
        for r, c in rocations:
            arr[r][c] = value


def solution(cadidate):
    # 사다리 0~3개 놨을 때
    for i in range(4):
        for temp in list(combinations(cadidate, i)): # 사다리 후보의 조합 0~4개
            if setSadary(temp, 1): # 사다리를 놓을 수 있으면
                if success() == 0: # 시잗-끝 다른 세로선이 없으면
                    return i # 그때의 사다리 갯수 출력
            setSadary(temp, 0) # 아니면 놓았던 사다리 빼기

    return -1 # 3개 놨는데도 안되면 -1 출력



N, M, H = q()
arr = [[0 for _ in range(N + 1)] for __ in range(H + 1)]
for _ in range(M):
    a, b = q()
    arr[a][b] = 1


cadidate = findCadidate() # 사다리를 놓을 수 있는 후보 위치

# 1개의 가로선을 두면 최대 2개의 결과가 바뀜
# 3개의 가로선을 두면 최대 6개의 결과가 바뀌는데, 바꿔야하는 결과가 6개 이상이면
# 3개 놔도 답없음
if success() > 6:
    print(-1)
else:
    print(solution(cadidate))
