import sys


sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]
dp = [[[987654321, 987654321] for _ in range(M)] for __ in range(N)]

for r in range(N):
    for c in range(M):
        if r == 0 and c == 0:
            dp[r][c][0] = 0
            dp[r][c][1] = 0
        elif r == 0:
            if arr[r][c] == 0:
                dp[r][c][0] = min(dp[r][c-1][0], dp[r][c-1][1]) + 1
            else:
                dp[r][c][1] = dp[r][c - 1][0] + 1
        elif c == 0:
            if arr[r][c] == 0:
                dp[r][c][0] = min(dp[r-1][c][0], dp[r-1][c][1]) + 1
            else:
                dp[r][c][1] = dp[r-1][c][0] + 1
        else:
            if arr[r][c] == 0:
                dp[r][c][0] = min(dp[r-1][c][0], dp[r-1][c][1], dp[r][c-1][0], dp[r][c-1][1]) + 1
            else:
                dp[r][c][1] = min(dp[r-1][c][0], dp[r][c-1][0]) + 1

for d in dp:
    print(d)


