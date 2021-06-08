import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())

def solution(n):
    arr = [[' ' for _ in range(n)] for _ in range(n)]

    k = 65

    for c in range(n//2, -1, -1):
        t = n//2 - c
        for r in range(n//2 - t, n//2 + t + 1):
            arr[r][c] = chr(k)
            k += 1
            if k > 90: k = 65


    for alphas in arr:
        print(*alphas)


if n < 1 or n > 100 or n % 2 == 0:
    print("INPUT ERROR")
else:
    solution(n)