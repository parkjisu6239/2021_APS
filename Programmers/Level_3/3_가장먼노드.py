def solution(n, edge):
    # 인접 딕셔너리
    vertexs = {i: [] for i in range(1, n + 1)}
    for e in edge:
        vertexs[e[0]].append(e[1])
        vertexs[e[1]].append(e[0])

    # 방문체크
    visit = [-1] * (n + 1)
    visit[1] = 0

    # 큐
    que = [1]

    # BFS
    while que:
        start = que.pop(0)

        for end in vertexs[start]:
            if visit[end] == -1:
                que.append(end)
                visit[end] = visit[start] + 1

    long_cnt = 0
    long = max(visit)
    for v in visit:
        if v == long:
            long_cnt += 1

    return long_cnt

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))