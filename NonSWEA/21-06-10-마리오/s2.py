import sys
sys.stdin = open('input.txt')

N = int(input())

arr = [0] + list(map(int, input().split())) + [0] * (N*2)
# 점프는 2칸 or 7칸 가능 -> 최고점 구하기

memo = [0] * (N*2)

def getPoint(n):
    if n == 0: return 0
    if n < 0: return -99999
    if memo[n]: return memo[n]


    a = getPoint(n-2)
    b = getPoint(n-7)

    result = max(a, b)

    memo[n] = result + arr[n]

    return memo[n]

Max = 0

for i in range(N + 1, N + 5):
    ans = getPoint(i)
    if ans > Max:
        Max = ans

print(Max)