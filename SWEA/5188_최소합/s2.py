import sys
import time
sys.stdin = open('eval_input.txt')
start = time.time()

def DP(arr):
    global cnt
    n = len(arr)
    for i in range(1, n):
        for j in range(1, n):
            cnt += 1
            if i == 1 or j == 1:
                arr[i][j] += max(arr[i - 1][j], arr[i][j - 1])
            else:
                arr[i][j] += min(arr[i - 1][j], arr[i][j - 1])



for tc in range(1, int(input())+1):
    N = int(input())

    arr = [[0] + list(map(int, input().split())) for i in range(N)]
    arr = [[0] * (N+1)] + arr

    cnt = 0

    DP(arr)
    print('#{} {} {}'.format(tc, arr[N][N], cnt))

print((time.time() - start)*1000) # 0.9989738464355469