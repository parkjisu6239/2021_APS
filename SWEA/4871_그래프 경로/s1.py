import sys
sys.stdin = open('eval_input.txt')


def DFS(v):
    while visited[target_end] == 0:
        # while문 들어왔는데(목표지점에 도착하지 않았는데), 스택이 비어있으면 종료
        if not stack:
            return 0
        # stack이 비어있지않고, 아직 그 정점을 방문하지 않은 경우
        elif visited[v] == 0:
            # 방문했다고 하고
            visited[v] = 1
            # 방문 했으니, 그 정점을 스택에서 빼자
            w = stack.pop()
            # 연결된 노드 중에
            for i in adjacency_list[w]:
                # 방문하지 않았으면 노드를 스택에 쌓아라
                if visited[i] == 0:
                    stack.append(i)

            # 스택이 비어있지 않다면, 가장 뒤에 있는 값으로 반복을 더 수행하고
            if stack:
                v = stack[-1]
            # 스택이 비어있다면
            else:
                # 목표지점에 방문했으면 1
                if visited[target_end]:
                    return 1
                # 목표지점에 방문하지 못했으면
                else:
                    return 0

        # 그 정점을 방문한 경우
        else:
            v = stack.pop()

    return 1


for tc in range(1, int(input()) +1):
    V, E = map(int,input().split())
    adjacency_list = [[] for _ in range(V+1) ]

    for _ in range(E):
        start, end = map(int, input().split())
        adjacency_list[start].append(end)

    target_start, target_end = map(int, input().split())

    visited = [ 0 for _ in range(V+1)]
    stack = [target_start]

    print('#{} {}'.format(tc, DFS(target_start)))

