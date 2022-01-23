import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
arr = [float(input().rstrip()) for _ in range(N)]

for i in range(1, N):
    arr[i] = max(arr[i], arr[i] * arr[i-1])
print("{:.3f}".format(max(arr)))
