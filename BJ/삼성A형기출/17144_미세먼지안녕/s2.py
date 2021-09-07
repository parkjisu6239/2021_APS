# [boj] 17144 미세먼지 안녕 https://www.acmicpc.net/problem/17144

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
    temp = []
    for r in range(R):
        for c in range(C):
            if arr[r][c] >= 5:
                temp.extend(adjacentDust(r, c))

    for r, c, dust in temp:
        arr[r][c] += dust


# 인접한 4방향 확인
def adjacentDust(r, c):
    temp = []
    adj = 0
    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]
        if 0 <= nr < R and 0 <= nc < C:
            if (nr, nc) in [(airCleaner, 0), (airCleaner+1, 0)]: continue
            temp.append((nr, nc, arr[r][c]//5))
            adj += 1

    temp.append((r, c, -(arr[r][c]//5)*adj))
    return temp


# 공기청정기 가동
def freshAirUp():
        k = 0
        r, c = airCleaner - 1, 0
        while True:
            nr, nc = r + dr[k], c + dc[k]
            if nr == airCleaner and nc == 0:
                arr[r][c] = 0
                break

            if 0 <= nc < C and 0 <= nr < airCleaner + 1:
                arr[r][c] = arr[nr][nc]
                r, c = nr, nc
                continue

            k += 1
            k %= 4


def freshAirDown():
    k = 2
    r, c = airCleaner + 2, 0
    while True:
        nr, nc = r + dr[k], c + dc[k]
        if nr == airCleaner + 1 and nc == 0:
            arr[r][c] = 0
            break

        if 0 <= nc < C and airCleaner + 1 <= nr < R:
            arr[r][c] = arr[nr][nc]
            r, c = nr, nc
            continue

        k -= 1
        k %= 4


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
