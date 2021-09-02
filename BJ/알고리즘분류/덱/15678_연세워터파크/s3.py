import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10 ** 6)

N, D = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
ans = -9999999999


def DFS(cnt, total, before):
    if cnt == N:
        return

    if total < dp[before]:
        return

    dp[before] = total

    end = before + D + 1 if before + D + 1 < N else N
    for i in range(before + 1, end):
        DFS(cnt + 1, total + arr[i % N], i % N)


for i in range(N):
    dp = [-9999999999] * (N + 1)
    DFS(1, arr[i], i)
    ans = max(ans, max(dp))

print(ans)