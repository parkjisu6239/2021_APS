import sys
from heapq import heappop, heappush

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
planet = [list(map(int, input().split())) for _ in range(N)]
visit = [0] * N
heap = [(0, 0)]
connect = 0
total_cost = 0

while heap:
    cost, v = heappop(heap)

    if visit[v]:
        continue

    visit[v] = 1
    connect += 1
    total_cost += cost

    if connect == N:
        break

    for w in range(N):
        if v == w:
            continue
        if visit[w]:
            continue
        heappush(heap, (planet[v][w], w))

print(total_cost)
