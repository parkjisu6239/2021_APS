import sys
from heapq import heappop, heappush
sys.stdin = open('input.txt')
input = sys.stdin.readline


tc = int(input())
for _ in range(tc):
    flag = 0
    N = int(input())
    arr = []
    for __ in range(N//10 + 1):
        arr.extend(list(map(int, input().split())))

    ans = []
    minH = [] # -중앙값 ~ -최솟값
    maxH = [] # 중앙값 ~ 최댓값

    print((N+1)//2)
    for idx, a in enumerate(arr):
        if len(minH) == len(maxH):
            heappush(maxH, -a)
        else:
            heappush(minH, a)

        if minH and minH[0] < -maxH[0]:
            mx = -heappop(maxH)
            mn = heappop(minH)
            heappush(maxH, -mn)
            heappush(minH, mx)

        if (idx + 1) % 2:
            flag += 1
            print(-maxH[0], end=' ')
            if flag % 10 == 0: print()
    print()
