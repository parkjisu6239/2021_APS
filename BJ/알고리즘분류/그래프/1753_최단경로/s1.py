import sys
sys.stdin = open('input.txt')

# input
V, E = map(int, input().split())
K = int(input())

# 인접행렬
graph = [[0]*(V+1) for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    if graph[u][v]:
        if w < graph[u][v]:
            graph[u][v] = w
    else:
        graph[u][v] = w

# 다익스트라 준비물
distance = [9999999] * (V+1)
distance[K] = 0
que = [K]

# 다익스트라 실행부
while que:
    v = que.pop()
    for w in range(V+1):
        if graph[v][w]:
            k_to_w = distance[v] + graph[v][w]
            if k_to_w < distance[w]:
                distance[w] = k_to_w
                que.append(w)

# output
for i in range(1, len(distance)):
    if distance[i] == 9999999:
        print('INF')
    else:
        print(distance[i])


