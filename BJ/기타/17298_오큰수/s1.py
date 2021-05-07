import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
DP = [-1] * N
max_val = nums[-1]

for i in range(N-2, -1, -1):
    if nums[i] < nums[i+1]:
        DP[i] = nums[i+1]
    elif nums[i] < DP[i+1]:
        DP[i] = DP[i+1]
    elif nums[i] < max_val:
        DP[i] = max_val
    else:
        DP[i] = -1
        max_val = nums[i]

print(*DP)
