# coding=utf-8
# boj 1655 가운데를 말해요
# 중앙값 찾는 문제
# 최대힙, 최소힙 두개 써서 비교하여 접근

import sys
from heapq import heappop, heappush

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
maxH = [] # -중앙값 ~ -최솟값
minH = [] # 중앙값 ~ 최댓값
for _ in range(N):
    x = int(input())
    if len(minH) < len(maxH):
        heappush(minH, x)
    else:
        heappush(maxH, -x)

    if minH and maxH and minH[0] < -maxH[0]:
        heappush(maxH, -heappop(minH))
        heappush(minH, -heappop(maxH))

    print(-maxH[0])