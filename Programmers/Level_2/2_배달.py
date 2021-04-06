from pandas import DataFrame as df
def solution(N, road, K):
    # <POINT>
    # 경우에 따라, 이미 방문한 정점을 다시 갈 수도 있다!
    # 노드 간의 거리가 다르기 때문에 depth가 깊더라도, 최단거리 일 수 있기 때문이다.
    # 그렇다면 모든 정점을 재방문 해야하는가? 그렇지 않다.
    # 최단거리를 갱신할 수 있는 경우에만 재방문 하고, 그때의 거리로 갱신한다.

    # 인접행렬을 만들고, 값은 정점 사이의 거리로 지정
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

    print(df(matrix))

    # visit은 1번 정점과의 최단거리로 지정할 것이기 때문에 초기값은 큰 수를 지정함.
    visit = [99999999999] * (N + 1)

    # DFS, BFS 상관 X
    que = [1]
    visit[1] = 0

    while que:
        v = que.pop(0)
        for i in range(len(matrix[v])):
            # 연결되어 있고, 현재 방문 경로가 최단 거리인 경우
            # matrix[v][i]:v정점과 i정점 사이의 거리, visit[v]:1번 정점과 v정점 사이의 거리
            if matrix[v][i] and matrix[v][i] + visit[v] < visit[i]:
                if visit[v] + matrix[v][i] <= K: # 이거 없어도 정답이지만 있으면 1초정도 빠름
                    que.append(i)
                    visit[i] = matrix[v][i] + visit[v]

    print(visit)
    result = 0
    for i in range(len(visit)):
        if visit[i] <= K:
            result += 1

    return result

print(solution(6, [[1,2,1],[1,3,4],[2,3,2],[3,4,1],[3,5,2],[3,5,3],[5,6,1]], 4))