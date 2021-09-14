# boj 1743 낚시왕
# d가 1인 경우는 위, 2인 경우는 아래, 3인 경우는 오른쪽, 4인 경우는 왼쪽을 의미

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

R, C, M = map(int, input().split())
arr = [[0] * C for _ in range(R)]
sharks = {}

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
    if d == 1: # 상
        if s <= r - 0:
            return r - s, c, d
        else:
           rd = s - r
           quo, remain = divmod(rd, R-1)
           if quo % 2 == 0: # 짝수번
               return remain, c, 2
           else:
               return R-1-remain, c, 1
    elif d == 2: # 하
        if s <= R-1-r:
            return r + s, c, d
        else:
            rd = s - (R-1-r)
            quo, remain = divmod(rd, R - 1)
            if quo % 2 == 0:  # 짝수번
                return R - 1 - remain, c, 1
            else:
                return remain, c, 2
    elif d == 3: # 좌
        if s <= C-1-c:
            return r, c + s, d
        else:
            cd = s - (C-1-c)
            quo, remain = divmod(cd, C - 1)
            if quo % 2 == 0:  # 짝수번
                return r, C - 1 - remain, 4
            else:
                return r, remain, 3
    else:
        if s <= c - 0:
            return r, c-s, d
        else:
           cd = s - c
           quo, remain = divmod(cd, C-1)
           if quo % 2 == 0: # 짝수번
               return r, remain, 3
           else:
               return r, C-1-remain, 4


def solution():
    total = 0

    for c in range(C):
        total += fishing_king(c)
        shark()

    return total

print(solution())