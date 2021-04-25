import sys
sys.stdin = open('input.txt')
from heapq import heappush, heappop

# 프림 #
while True:
    V, E = map(int, input().split())

    if V == 0 and E == 0:
        break

    graph = [[] for _ in range(V)]
    total = 0

    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((w, e))
        graph[e].append((w, s))
        total += w


    visit = [0] * V
    min_tree = 0

    heap = []
    heappush(heap, (0, 0))
    node = 0

    while heap:
        path_v_d, v = heappop(heap)

        if visit[v]:
            continue

        visit[v] = 1
        node += 1
        min_tree += path_v_d

        for v_w_d, w in graph[v]:
            if visit[w] == 0:
                heappush(heap, (v_w_d, w))

    print(total-min_tree)



