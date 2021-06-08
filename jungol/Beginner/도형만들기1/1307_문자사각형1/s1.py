import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())

arr = [['' for _ in range(n)] for _ in range(n)]
k = 65

for c in range(n-1, -1, -1):
    for r in range(n-1, -1, -1):
        arr[r][c] = chr(k)
        k += 1
        if k > 90: k = 65

for alphas in arr:
    print(*alphas)