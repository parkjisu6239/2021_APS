import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

R, C = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(R)]
cave = arr[::-1]
N = int(input())
height = list(map(int, input().split()))
visited = [[0] * C for _ in range(R)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def bfs(r, c):
    global visited
    que = [[r, c]]
    temp = [[r, c]]
    visited[r][c] = 1

    while que:
        r, c = que.pop(0)

        for k in range(4):
            ncr, ncc = r + dr[k], c + dc[k]

            if ncr < 0 or ncr > R - 1:
                continue

            if ncc < 0 or ncc > C - 1:
                continue

            if visited[ncr][ncc]:
                continue

            if cave[ncr][ncc] == '.':
                continue

            if ncr == 0:
                return []

            visited[ncr][ncc] = 1
            que.append([ncr, ncc])
            temp.append([ncr, ncc])

    return temp


def get_cluster(r, c):
    global visited

    cave[r][c] = '.'
    visited = [[0] * C for _ in range(R)]
    clusters = []

    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]

        if nr < 0 or nr > R - 1:
            continue

        if nc < 0 or nc > C - 1:
            continue

        if visited[nr][nc]:
            continue

        if cave[nr][nc] == '.':
            continue

        clusters.extend(bfs(nr, nc))

    return clusters


def falling(floating):
    if not floating:
        return 0

    floating.sort()

    while True:
        flag = -1
        for idx, [r, c] in enumerate(floating):
            nr = r - 1
            if nr < 0 or cave[nr][c] == 'x':
                flag = idx
                break

            cave[r][c], cave[nr][c] = cave[nr][c], cave[r][c]
            floating[idx][0] -= 1

        if flag != -1:
            for i in range(flag):
                r, c = floating[i]
                cave[r][c], cave[r+1][c] = cave[r+1][c], cave[r][c]

            return


for idx, h in enumerate(height):
    if idx % 2 == 0: # 좌
        c = 0
        while c < C and cave[h-1][c] != 'x':
            c += 1
    else: # 우
        c = C-1
        while c > 0 and cave[h-1][c] != 'x':
            c -= 1

    if 0 <= c < C:
        cluster = get_cluster(h - 1, c)
        falling(cluster)


for row in range(R-1, -1, -1):
    print(*cave[row])
