import sys
sys.stdin = open('input.txt', 'r')
q = lambda: map(int, sys.stdin.readline().split())

N, M = q()
arr = [list(q()) for _ in range(N)]

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

max_one = max(map(max, arr))
MAX = 0

visit = [[0] * M for _ in range(N)]

def DFS(r, c, depth, total):
    global MAX

    # 남은게 모두 최대값이여도 MAX보다 작으면 유망하지 않음
    if total + (4 - depth)*max_one < MAX:
        return

    if depth == 4:
        MAX = max(MAX, total)
        return

    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < N and 0 <= nc < M and visit[nr][nc] == 0:
            if depth == 2:
                visit[nr][nc] = 1
                DFS(r, c, depth+1, total+arr[nr][nc])
                visit[nr][nc] = 0

            visit[nr][nc] = 1
            DFS(nr, nc, depth + 1, total + arr[nr][nc])
            visit[nr][nc] = 0


for r in range(N):
    for c in range(M):
        visit[r][c] = 1
        DFS(r, c, 1, arr[r][c])
        visit[r][c] = 0

print(MAX)