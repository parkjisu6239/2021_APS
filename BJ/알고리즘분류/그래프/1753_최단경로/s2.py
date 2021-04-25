import sys
from heapq import heappush, heappop
sys.stdin = open('input.txt')

# input
V, E = map(int, input().split())
K = int(input())

# 인접행렬
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))


# 다익스트라 준비물
distance = [9999999] * (V+1)
distance[K] = 0
visit = [0] * (V+1)
que = []
heappush(que, (0, K))

# 다익스트라 실행부
while que:
    k_to_v, v = heappop(que)

    if visit[v]:
        continue
    visit[v] = 1

    for v_to_w, w in graph[v]:
        k_to_w = distance[v] + v_to_w
        if k_to_w < distance[w]:
            distance[w] = k_to_w
            heappush(que, (k_to_w, w))

# output
for i in range(1, len(distance)):
    if distance[i] == 9999999:
        print('INF')
    else:
        print(distance[i])


