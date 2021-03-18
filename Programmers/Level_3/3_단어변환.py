def solution(begin, target, words):
    # BFS이지만, 인접리스트로 표현하기 위한 방법이 포인트!

    visit = [-1] * (len(words)+2)
    node = [begin] + words
    vertex = { i: [] for i in range(len(node))}

    # 타겟이 words안에 없으면 0, 종점 위치 찾아두기
    if target in node:
        n = node.index(target)
    else:
        return 0

    # 인접 딕셔너리 만들기
    for i in range(len(node)-1):
        for j in range(len(node)):
            if i != j:
                diffrent = 0
                for k in range(len(begin)):
                    if node[i][k] != node[j][k]:
                        diffrent += 1
                    if diffrent > 1:
                        break
                else:
                    vertex[i].append(j)

    # 큐, 방문체크
    que = [0]
    visit[0] = 0

    # BFS
    while que:
        # 종점 방문했다면, 그때의 거리 출력
        if visit[n] != -1 :
            return visit[n]

        start = que.pop(0)

        for end in vertex[start]:
            if visit[end] == -1:
                que.append(end)
                visit[end] = visit[start] + 1

    return visit[n]


print(solution("hit", "cog", ["dog", "lot", "hot", "dot", "log", "cog"]))