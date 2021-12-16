import sys
from heapq import heappush, heappop

sys.stdin = open('input.txt')
input = sys.stdin.readline

heap = list()
N = int(input())

for _ in range(N):
    x = int(input())
    if x == 0:
        if heap:
            print(heappop(heap)[1])
        else:
            print(0)
    else:
        heappush(heap, (abs(x), x))
