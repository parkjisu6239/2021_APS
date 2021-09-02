import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10 ** 6)

N, D = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
dp = [0] * N
dp[0] = arr[0]

for i in range(1, N):
    for jump in range(1, D+1):
        if i - jump >= 0:
            dp[i] = max(dp[i-jump] + arr[i], dp[i])

print(max(dp))




