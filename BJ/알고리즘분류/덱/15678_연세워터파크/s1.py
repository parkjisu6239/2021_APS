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

    for i in range(N):
        if visit[i] == 0 and abs(before - i) <= D:
            visit[i] = 1
            DFS(cnt + 1, total + arr[i], i)
            visit[i] = 0



for i in range(N):
    dp = [-9999999999] * (N + 1)
    visit = [0] * N
    visit[i] = 1
    DFS(1, arr[i], i)
    ans = max(ans, max(dp))

print(ans)