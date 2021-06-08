import sys
from heapq import heappush, heappop
sys.stdin = open('eval_input.txt')


# ① 1~must1~must2~n
# ② 1~must2~must1~n
# 답 min(①, ②)


def dijkstra(start, end):
    visit = [0] * (V + 1)
    distance = [1001] * (V + 1)
    distance[start] = 0

    heap = []
    heappush(heap, (0, start))

    while heap:
        one_to_v, v = heappop(heap)

        if visit[v]:
            continue
        visit[v] = 1

        for v_w, w in graph[v]:
            one_to_w = one_to_v + v_w
            if one_to_w < distance[w]:
                distance[w] = one_to_w
                heappush(heap, (one_to_w, w))

    return distance[end]


V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]

for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s].append((w, e))
    graph[e].append((w, s))

must1, must2 = map(int, input().split())

# ① 1~must1~must2~n
# ② 1~must2~must1~n
# 중간 경로가 없으면 dijkstra의 결과값은 초기값인 1001

result1 = dijkstra(1, must1) + dijkstra(must1, must2) + dijkstra(must2, V)
result2 = dijkstra(1, must2) + dijkstra(must2, must1) + dijkstra(must1, V)

if result1 >= 1001 and result1 >= 1001:
    print(-1)
else:
    print(min(result1, result2))
