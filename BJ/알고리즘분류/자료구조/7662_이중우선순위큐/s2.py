import sys
from heapq import heappop, heappush
sys.stdin = open('input.txt')
input = sys.stdin.readline


T = int(input())

for _ in range(T):
    K = int(input())
    maxH, minH = [], []
    visit = [1] * (K+1)
    for k in range(K):
        cmd, val = map(str, input().split())
        val = int(val)
        if cmd == "I":
            heappush(minH, (val, k))
            heappush(maxH, (-val, k))
        elif val == 1:
            while maxH and not visit[maxH[0][1]]:
                heappop(maxH)
            if maxH:
                visit[maxH[0][1]] = 0
                heappop(maxH)
        else:
            while minH and not visit[minH[0][1]]:
                heappop(minH)
            if minH:
                visit[minH[0][1]] = 0
                heappop(minH)
    while minH and not visit[minH[0][1]]:
        heappop(minH)
    while maxH and not visit[maxH[0][1]]:
        heappop(maxH)

    if maxH and minH:
        print(-maxH[0][0], minH[0][0])
    else:
        print('EMPTY')