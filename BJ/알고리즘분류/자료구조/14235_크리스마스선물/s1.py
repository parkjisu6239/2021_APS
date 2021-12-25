import sys
from heapq import heappop, heappush

sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
present = []

for _ in range(n):
    read = list(map(int, input().split()))
    if read[0] == 0: # 선물주기
        if present:
            print(-heappop(present))
        else:
            print(-1)
    else:
        for r in read[1:]:
            heappush(present, -r)