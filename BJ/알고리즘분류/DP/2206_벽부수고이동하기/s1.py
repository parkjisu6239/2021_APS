import sys
sys.setrecursionlimit(500000000)


sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]
visited = [[0] * M for _ in range(N)]
arr = [list(map(int, input().rstrip())) for _ in range(N)]
ans = 987654321
dp = [[[987654321] * M for _ in range(N)] for _ in range(2)]


def dfs(r, c, cnt, smash):
    global ans

    if cnt >= dp[smash][r][c]:
        return

    dp[smash][r][c] = cnt

    if cnt >= ans:
        return

    if r == N-1 and c == M-1:
        ans = min(ans, cnt)
        return

    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]
        if is_out(nr, nc):
            continue

        if visited[nr][nc]:
            continue

        if arr[nr][nc] == 0:
            visited[nr][nc] = 1
            dfs(nr, nc, cnt + 1, smash)
            visited[nr][nc] = 0
        elif smash:
            visited[nr][nc] = 1
            dfs(nr, nc, cnt + 1, 0)
            visited[nr][nc] = 0


def is_out(r, c):
    if 0 <= r < N and 0 <= c < M:
        return False
    return True


visited[0][0] = 1
dfs(0, 0, 1, 1)
print(ans if ans != 987654321 else -1)