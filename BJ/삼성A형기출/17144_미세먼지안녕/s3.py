# [boj] 17144 미세먼지 안녕 https://www.acmicpc.net/problem/17144
# 37ms

import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]

# 시계방향
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


# 0열에 있는 공기청정기 위치 찾기
def findAirCleaner():
    for r in range(R):
        if arr[r][0] == -1:
            return r


# 미세먼지 확산
def spreadDust():
    # temp로 두고 que나 list에 append 해도 되는데 이렇게 하는게 10배 빠름
    # 매번 append, pop 하는 동작은 최대한 지양하는 것이 좋을 듯!
    new = [[0 for _ in range(C)] for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if arr[i][j] >= 5:
                each = arr[i][j] // 5
                count = 0
                for k in range(4):
                    ndr = i + dr[k]
                    ndc = j + dc[k]
                    if 0 <= ndr < R and 0 <= ndc < C and arr[ndr][ndc] != -1:
                        count += 1
                        new[ndr][ndc] += each
                arr[i][j] = arr[i][j] - count * each

    for i in range(R):
        for j in range(C):
            arr[i][j] += new[i][j]


# 공기청정기 가동
def freshAirUp():
    for i in range(airCleaner-1, 0, -1):
        arr[i][0] = arr[i-1][0]

    for j in range(0, C-1):
        arr[0][j] = arr[0][j+1]

    for i in range(0, airCleaner):
        arr[i][C-1] = arr[i+1][C-1]

    for j in range(C-1, 1, -1):
        arr[airCleaner][j] = arr[airCleaner][j-1]

    arr[airCleaner][1] = 0


def freshAirDown():
    for i in range(airCleaner + 2, R-1):
        arr[i][0] = arr[i + 1][0]

    for j in range(0, C - 1):
        arr[R-1][j] = arr[R-1][j + 1]

    for i in range(R-1, airCleaner+1, -1):
        arr[i][C - 1] = arr[i - 1][C - 1]

    for j in range(C - 1, 1, -1):
        arr[airCleaner+1][j] = arr[airCleaner+1][j - 1]

    arr[airCleaner+1][1] = 0


# 남은 먼지 수 세기
def countDust():
    cnt = 0
    for r in range(R):
        for c in range(C):
            if arr[r][c] > 0:
                cnt += arr[r][c]

    return cnt


airCleaner = findAirCleaner() # 공기청정기 위치

for _ in range(T):
    spreadDust()
    freshAirUp()
    freshAirDown()

print(countDust())
