import sys
from heapq import heappop, heappush

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
planet = [list(map(int, input().split())) for _ in range(N)]
visit = [0] * N
connect_cost = [100000000] * N
heap = [(0, 0)]
connect = 0
connect_cost[0] = 0

while heap:
    cost, v = heappop(heap)

    if visit[v]:
        continue
    if cost > connect_cost[v]:
        continue

    visit[v] = 1
    connect += 1

    if connect == N:
        break

    for w in range(N):
        if v == w:
            continue
        if visit[w]:
            continue
        if planet[v][w] < connect_cost[w]:
            connect_cost[w] = planet[v][w]
            heappush(heap, (planet[v][w], w))

print(sum(connect_cost))
