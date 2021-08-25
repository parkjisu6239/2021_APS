import sys
sys.stdin = open('input.txt')

memo = {0: 0, 1: 1}
dp = {0: [1, 0], 1: [0, 1]}

# 76ms

def fibo(n):
    if n in memo:
        return memo[n]

    memo[n] = fibo(n-1) + fibo(n-2)
    dp[n] = [dp[n-1][0] + dp[n-2][0], dp[n-1][1] + dp[n-2][1]]
    return memo[n]


tc = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readlines()))
MAX = max(arr)

fibo(MAX)
for num in arr:
    print(*dp[num])
