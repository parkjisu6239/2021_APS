import sys
sys.stdin = open('eval_input.txt')


def BFS(que, G, node):
    # 시점과의 거리
    distance = 1
    # 큐가 비어있지 않을 때 반복
    while que:
        # 목적지에 도착했으면 종료
        if visited[G]:
            return visited[G]

        v = que.pop(0)
        for w in node[v]:
            if not visited[w]:
                que.append(w)
                visited[w] = distance

        # 거리를 올려주는 경우
        # 같은 거리인 정점이 여러개 큐에 있는 경우에는
        # 큐가 빠질때마다 거리를 올려주는게 아니라,
        # 동일 거리인 정점이 다 빠지고 나서 거리를 올려줌
        if que and visited[v] != visited[que[0]]:
            distance += 1

    # 큐가 비었으면 종료
    return visited[G]

# 최단거리 구하기
for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    # 인접 딕셔너리
    node = { i : [] for i in range(V+1)}
    for _ in range(E):
        s, e = map(int, input().split())
        node[s].append(e)
        node[e].append(s)
    S, G = map(int, input().split())

    que = [S]
    visited = [0] * (V+1)
    visited[S] = -1

    print('#{} {}'.format(tc, BFS(que, G, node)))


