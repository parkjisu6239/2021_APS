import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())

arr = [[' ' for _ in range(n)] for _ in range(n)]

k = 65

for r in range(n):
    for t in range(n-r):
        arr[r+t][n-1-t] = chr(k)
        k += 1
        if k > 90: k = 65

for alphas in arr:
    print(*alphas)