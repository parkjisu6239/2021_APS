import sys
from heapq import heappop, heappush
sys.stdin = open('input.txt')
input = sys.stdin.readline


tc = int(input())
for _ in range(tc):
    N = int(input())
    arr = []
    for __ in range(N//10 + 1):
        arr.extend(list(map(int, input().split())))

    ans = []
    maxH = [] # 중앙값 ~ 최댓값
    minH = [] # -중앙값 ~ -최솟값
    for idx, a in enumerate(arr):
        if not maxH and not minH:
            heappush(maxH, a)
        elif len(minH) < len(maxH):
            if a > maxH[0]:
                heappush(minH, -heappop(maxH))
                heappush(maxH, a)
            else:
                heappush(minH, -a)
        else:
            if a < maxH[0]:
                heappush(minH, -a)
                heappush(maxH, -heappop(minH))
            else:
                heappush(maxH, a)

        if idx % 2 == 0:
            ans.append(maxH[0])

    print(len(ans))
    for cnt in range(len(ans)//10 + 1):
        print(*ans[10*cnt: 10*cnt + 10])
