import sys
sys.stdin = open('eval_input.txt')

# 프림 #
for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    graph = [[0] * (V+1) for _ in range(V+1)] # 0~V

    for i in range(E): # 인접행렬
        s, e, w = map(int, input().split())
        graph[s][e] = w
        graph[e][s] = w

    connect_E = 0 # 연결한 엣지 수
    visit = [0] * (V + 1) # 방문체크
    distance = [987654321] * (V+1) # 거리 갱신

    v = 0 # 시작 아무거나 상관없지만 일반적으로 0
    distance[v] = 0
    visit[v] = 1

    while connect_E < V:
        for w in range(V + 1):
            # 방문하지 않았고, 연결되어 있고, 거리 갱신 가능하면
            if visit[w] == 0 and graph[v][w] and graph[v][w] < distance[w]:
                distance[w] = graph[v][w] # 거리 갱신

        min_d = 987654321
        for i in range(len(distance)):
            if distance[i] < min_d and visit[i] == 0: # 노방문 정점중, 거리가 가장 작은
                min_d = distance[i]
                v = i # 다음 경유지로 선택

        visit[v] = 1
        connect_E += 1


    print('#{} {}'.format(tc, sum(distance)))


