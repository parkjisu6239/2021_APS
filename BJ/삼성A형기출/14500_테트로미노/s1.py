import sys
sys.stdin = open('input.txt', 'r')
q = lambda: map(int, sys.stdin.readline().split())

N, M = q()
arr = [list(q()) for _ in range(N)]

poly = [[(0, 1), (0, 2), (0, 3)], [(1, 0), (2, 0), (3, 0)],
        [(1, 0), (0, 1), (1, 1)],
        [(1, 0), (2, 0), (2, 1)], [(1, 0), (2, 0), (2, -1)], [(0, 1), (1, 1), (2, 1)], [(0, 1), (1, 0), (2, 0)],
        [(1, 0), (1, 1), (1, 2)], [(0, 1), (0, 2), (-1, 2)], [(-1, 0), (-1, 1), (-1, 2)], [(0, 1), (0, 2), (1, 2)],
        [(1, 0), (1, 1), (2, 1)], [(0, 1), (-1, 1), (-1, 2)], [(-1, 0), (-1, 1), (-2, 1)], [(0, 1), (1, 1), (1, 2)],
        [(0, 1), (0, 2), (1, 1)], [(-1, 1), (0, 1), (1, 1)], [(0, 1), (-1, 1), (0, 2)], [(1, 0), (2, 0), (1, 1)]]


def isOk(r, c, idx):
    for dr, dc in poly[idx]:
        nr, nc = r + dr, c + dc
        if not (0 <= nr < N and 0 <= nc < M):
            return False
    return True


def getSum(r, c, idx):
    temp = arr[r][c]
    for dr, dc in poly[idx]:
        nr, nc = r + dr, c + dc
        temp += arr[nr][nc]

    return temp


MAX = 0
for r in range(N):
    for c in range(M):
        for idx in range(len(poly)):
            if isOk(r, c, idx):
                MAX = max(MAX, getSum(r, c, idx))

print(MAX)