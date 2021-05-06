import sys
from heapq import heappop, heappush
sys.stdin = open('input.txt')
input = sys.stdin.readline

V = int(input())
tree = [[] for _ in range(V+1)]
for _ in range(V-1):
    p, c, w = map(int, input().split())
    tree[p].append((w, c))
    tree[c].append((w, p))

def Dijkstra(s):
    heap = []
    heappush(heap, (0, s))
    distance = [9999999999] * (V+1)
    distance[s] = 0

    while heap:
        s_to_v, v = heappop(heap)

        for v_to_w, w in tree[v]:
            s_to_w = s_to_v + v_to_w
            if s_to_w < distance[w]:
                distance[w] = s_to_w
                heappush(heap, (s_to_w, w))

    return max(distance[1:])

result = 0
for start in range(1, V+1):
    result = max(result, Dijkstra(start))

print(result)
