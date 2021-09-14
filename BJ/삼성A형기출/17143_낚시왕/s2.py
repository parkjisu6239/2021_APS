# boj 1743 낚시왕
# d가 1인 경우는 위, 2인 경우는 아래, 3인 경우는 오른쪽, 4인 경우는 왼쪽을 의미

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

R, C, M = map(int, input().split())
arr = [[0] * C for _ in range(R)]
sharks = {}
dir = {1: (-1, 0), 2: (1, 0), 3: (0, 1), 4: (0, -1)}

for idx in range(1, M+1):
    r, c, s, d, z = map(int, input().split())
    arr[r-1][c-1] = idx
    sharks[idx] = (r-1, c-1, s, d, z)


def fishing_king(fc): # 상어 잡기
    for sr in range(R):
        if arr[sr][fc]:
            shark = arr[sr][fc]
            arr[sr][fc] = 0
            size = sharks[shark][4]
            del sharks[shark]
            return size
    return 0


def shark():
    for key, value in sharks.items(): # 이동
        r, c, s, d, z = value
        nr, nc, nd = move_shark(r, c, s, d)
        sharks[key] = (nr, nc, s, nd, z)
        arr[r][c] = 0

    for key, value in sharks.items(): # 잡아먹기
        r, c, s, d, z = value
        if arr[r][c]:
            if z < sharks[arr[r][c]][4]:
                continue
        arr[r][c] = key


def move_shark(r, c, s, d):
    i = 0
    while i < s:
        (nr, nc) = r + dir[d][0], c + dir[d][1]
        if 0 <= nr < R and 0 <= nc < C:
            r, c = nr, nc
        else:
            if d == 1 or d == 3: d += 1
            else: d -= 1
            continue
        i += 1

    return r, c, d

def solution():
    total = 0

    for c in range(C):
        total += fishing_king(c)
        shark()

    return total

print(solution())