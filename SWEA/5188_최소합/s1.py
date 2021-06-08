import sys
import time
sys.stdin = open('eval_input.txt')
start = time.time()

def min_sum(r, c, total):
    global min_val, cnt
    cnt += 1
    if r == N-1 and c == N-1:
        if total < min_val:
            min_val = total
        return

    if  total > min_val:
        return

    # 아래
    if r + 1 < N and c < N:
        total += arr[r+1][c]
        min_sum(r+1, c, total)
        total -= arr[r + 1][c]

    # 오른쪽
    if r < N and c + 1 < N:
        total += arr[r][c+1]
        min_sum(r, c+1, total)
        total -= arr[r][c + 1]


for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    cnt = 0
    min_val = 99999
    min_sum(0, 0, arr[0][0])
    print('#{} {} {}'.format(tc, min_val, cnt))

print((time.time() - start)*1000) # 1.0023117065429688