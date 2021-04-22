import sys
sys.stdin = open('input.txt')

# 프림 #
V = int(input())
E = int(input())
graph = [[987654] * (V+1) for _ in range(V+1)] # 초기값 무한

for i in range(E): # 인접정점인 경우 graph 갱신
    s, e, w = map(int, input().split())
    graph[s][e] = w
    graph[e][s] = w

v = 1 # 1번부터 시작(다른데서 시작해도 값은 같음)
distance = [987654] * (V+1) # 초기값 무한
distance[v] = 0 # 자기자신과의 거리 0
visit = [0]*(V+1)
visit[v] = 1 # 방문체크
node = 0

while node < V:
    for w in range(len(graph[v])): # 인접 정점 중에서
        if visit[w] == 0 and graph[v][w] < distance[w]: # 노방문, 거리 갱신
            distance[w] = graph[v][w]

    min_d = 987654
    for i in range(1, V+1): # 전체 거리정보중에서
        if visit[i] == 0 and distance[i] < min_d: # 노방문 가장 가깝
            min_d = distance[i]
            v = i

    visit[v] = 1
    node += 1


print(sum(distance[1:]))





