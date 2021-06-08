import sys
sys.stdin = open('eval_input.txt')


for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    graph = [[987654321] * (V+1) for _ in range(V+1)] # 0~V

    for i in range(E): # 인접행렬
        s, e, w = map(int, input().split())
        graph[s][e] = w

    visit = [987654321] * (V + 1) # 초기값 무한
    visit[0] = 0 # 0~0거리는 0

    # Dijkstra
    for v in range(V+1): # 0번부터 시작
        for w in range(V+1): # 인접 정점중에서
            if visit[v] + graph[v][w] < visit[w]: # 경유지로 가는게 더 짧다면
                visit[w] = visit[v] + graph[v][w] # 거리 갱신

    print(visit)
    print('#{} {}'.format(tc, visit[V]))


