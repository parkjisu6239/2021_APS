import sys
sys.stdin = open('input.txt')

N = int(input())

arr = list(map(int, input().split()))
arr = arr
# 점프는 2칸 or 7칸 가능 -> 최고점 구하기

memo = [0] * (N**2)

def getPoint(n):
    if n < 0: return -99999999
    if n == 0: return 0
    if memo[n]: return memo[n]

    a = getPoint(n-2)
    b = getPoint(n-7)

    result = max(a, b)

    memo[n] = result + arr[n]

    return result + arr[n]

max_point = -987654321

for i in range(1, 6):
    ans = getPoint(N+i)
    if ans > max_point:
        max_point = ans


print(max_point)