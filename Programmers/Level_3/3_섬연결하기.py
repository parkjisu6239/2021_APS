def solution(n, costs):
    # 노드가 n개 일때 모든 정점을 연결하려면 간선은 n-1개가 있어야 한다.
    answer = 0
    costs.sort()
    graph = [[0] * n for _ in range(n)]
    bridge = 0
    for cost in costs:
        if graph[cost[0]][cost[1]] == 0 or graph[cost[0]][cost[1]] < cost[2]:
            graph[cost[0]][cost[1]] = cost[2]
            graph[cost[1]][cost[0]] = cost[2]

    return graph

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))