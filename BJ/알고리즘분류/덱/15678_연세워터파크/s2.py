import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('input.txt')

N, D = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
ans = -9999999999

def DFS(cnt, total, before):
    if cnt == N:
        return

    if total < dp[cnt]:
        return

    dp[cnt] = total

    start = before - D if before - D > 0 else 0
    end = before + D + 1 if before + D + 1 < N else N

    for i in range(start, end):
        if visit[i%N] == 0:
            visit[i%N] = 1
            DFS(cnt + 1, total + arr[i%N], i%N)
            visit[i%N] = 0



for i in range(N):
    dp = [-9999999999] * (N + 1)
    visit = [0] * N
    visit[i] = 1
    DFS(1, arr[i], i)
    ans = max(ans, max(dp))

print(ans)