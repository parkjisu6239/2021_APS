def still_connect(start, end, node):
    # 만약 건설 비용이 비싼 다리가 없어도, 여전이 그 정점 사이의 경로가 존재한다면,
    # 이 비싼 다리는 없어도 된다.
    # 그래서 그 비싼걸 제거해보자
    node[start].remove(end)
    node[end].remove(start)

    # 만약 제거 했는데도
    que = [start] # 시점에서 출발해서
    visit = [0] * len(node)
    while que:
        pos = que.pop(0)

        for p in node[pos]:
            # 종점에 왔다면
            if p == end:
                # 이 경로를 제거해도 여전히 연결되어있다(True)
                return True

            if visit[p] == 0:
                visit[p] = 1
                que.append(p)

    # 하지만, 종점에 도달하지 못한다면
    # 이 경로는 아무리 비싸도 없어서는 안된다.
    # 그러니까 다시 원상복구 해주자
    node[start].append(end)
    node[end].append(start)
    return False


def solution(n, costs):
    # idea
    # 인풋으로 주어지는 연결은 최소가 아니다.
    # 만약 특정 연결이 없어도 그 정점 사이를 갈 수 있는 경로가 있다면, 그 연결은 없어도 된다.
    # 모든 정점이 연결되기 위해서는 최소 간선이 n-1개 있어야 한다

    # 그리디는 보통 정렬이 되어 있어야 하더라? 선형적으로 한번만 보기 때문인듯
    # 비용이 비싼 순으로 정렬한다. 그 연결이 없어도 되면 제거하기 위해서
    costs.sort(key=lambda x: (-x[2]))

    # 연결 리스트
    node = [[] for _ in range(n)]
    for i in range(len(costs)):
        node[costs[i][0]].append(costs[i][1])
        node[costs[i][1]].append(costs[i][0])

    # 간선 수
    m = len(costs)
    # 총 비용
    total = 0

    for i in range(len(costs)):
        # 간선수가 n-1이면 이후로 나오는 것들은 뺄 수가 없음
        if m ==  n - 1:
            total += costs[i][2]
            continue

        # 여전히 연결되어 있는가?
        if still_connect(costs[i][0], costs[i][1], node):
            # 이 경로는 필요 없으니 간선수도 -1 해준다
            m -= 1
            continue
        # 이 경로를 빼면 안된다.
        else:
            # 그렇다면 건설해야하니 건설 비용을 더한다.
            total += costs[i][2]

    return total

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))