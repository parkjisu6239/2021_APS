import sys
sys.stdin = open('input.txt')


def DFS(v, d):
    global min_d
    # 다 방문했고, 가장 마지막 방문이 V번 정점
    if visit[must1] and visit[must2] and visit[V] and v == V: # 다 방문
        min_d = min(min_d, d)
        return

    if d > min_d:
        return

    for v_w_d, w in graph[v]:
        if visit[w] == 0:
            visit[w] = 1
            DFS(w, d+v_w_d)
            visit[w] = 0


V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]

for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s].append((w, e))
    graph[e].append((w, s))

must1, must2 = map(int, input().split())

visit = [0] * (V+1)
visit[1] = 1
min_d = 9999999

DFS(1, 0)

print(min_d)
