import sys
sys.stdin = open('eval_input.txt')
input = sys.stdin.readline

def DP(N):
    if N < len(memo):
        return memo[N]
    memo.append(DP(N-1) + DP(N-2) + DP(N-3))
    return memo[N]

for tc in range(1, int(input())+1):
    N = int(input())
    memo = [0, 1, 2, 4]
    print(DP(N))

