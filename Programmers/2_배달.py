def solution(N, road, K):
    # 인접행렬의 원소를 거리로 만들자
    matrix = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    # 인접 행렬 생성
    for i in range(len(road)):
        v, w, d = road[i][0], road[i][1], road[i][2]
        # 0인 경우 바로 값 넣기
        if not matrix[v][w]:
            matrix[v][w] = d
            matrix[w][v] = d
        # 예제에서 같은 정점인데 거리가 2번 이상 주어지는 경우, 작은값으로 넣기 위함
        else:
            if d < matrix[v][w]:
                matrix[v][w] = d
                matrix[w][v] = d

    print(matrix)
    result = 1
    visit = [0] * (N + 1)

    que = [[1, 0]]
    visit[1] = 1

    while que:
        v, d = que.pop(0)
        for i in range(len(matrix[v])):
            # 연결되어 있고, 방문하지 않았고, 거리가 k 이하
            if matrix[v][i] and not visit[i]:
                que.append([i, matrix[v][i]+d])
                visit[i] = matrix[v][i]+d
                result += 1

    print(visit)
    return result

print(solution(6, [[1,2,1],[1,3,3],[2,3,1],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))