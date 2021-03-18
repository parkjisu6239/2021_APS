def solution(n, computers):
    # DFS 탐색 : 단 스택이 비면, 다른 시작 지점을 찾아서 재탐색

    # 인접 딕셔너리
    node = { i : [] for i in range(n)}
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j]:
                node[i].append(j)

    # 방문체크, 시작점으할 정점 후보, 스택, 네트워크 수
    visit = [0] * n
    candidate = list(range(1, n))
    stack = [0]
    network = 0

    # DFS
    while visit != [1] * n: # 모든 정점을 방문할때까지
        network += 1

        while stack:
            start = stack.pop()
            visit[start] = 1

            for end in node[start]:
                if visit[end] == 0:
                    stack.append(end)
                    visit[end] = 1
                    candidate.remove(end)

        # 더 이상 갈곳이 없으면, 새로운 시작점으로 DFS 재탐색
        if candidate:
            stack.append(candidate.pop(0))
        else:
            return network



print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))