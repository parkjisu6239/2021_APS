def solution(n, costs):
    # 인접행렬 node[v][w] = d
    node = [[99999999] * n for _ in range(n)]
    for v, w, d in costs:
        node[v][w] = d
        node[w][v] = d

    # 탐색 경로, 방문 체크
    route = [0]
    visit = [0]*n
    visit[0] = 1

    # 최소신장트리의 길이
    result = 0

    # 모든 정점을 순회할때까지
    while len(route) < n:
        min_d = 99999999
        # 경로에 있는 정점 v
        for v in route:
            # v와 연결된 w중에서
            for w in range(n):
                # 방문하지 않았고, 가깝다면 다음 방문지로 임시 지정
                if not visit[w] and node[v][w] < min_d:
                    min_d = node[v][w]
                    min_v = w

        # 루트 자체와 가장 가까운 정점을 찾은 후
        visit[min_v] = 1 # 방문체크
        result += min_d # 길이 추가
        route.append(min_v) # 경로에 추가

    return result


print(solution(4, [[0,1,1],[0,3,2],[1,2,3],[1,3,2],[2,3,4]]))