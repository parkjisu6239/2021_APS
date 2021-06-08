import sys
sys.stdin = open('eval_input.txt')

def IsConnect():
    # DFS를 위한 변수 생성
    visited = [0] * 100
    stack = [0]
    visited[0] = 1

    # stack에 값이 있다면 반복
    while stack:
        # 방문하려는 정점이 99이면, 갈수있는거니까 1반환
        if stack[-1] == 99:
            return 1

        # 빼서 방문체크
        v =  stack.pop()
        visited[v] = 1

        # 현재 정점에서 갈 수 있는 곳중에
        if adjacency_dict.get(v, -1) != -1:
            for connect in adjacency_dict[v]:
                # 방문하지 않은 곳을 스택에 쌓기
                if not visited[connect] :
                    stack.append(connect)

    if visited[99]:
        return 1
    else:
        return 0


for _ in range(10):
    # 입력
    tc, node = map(int, input().split())
    node_list = list(map(int, input().split()))

    # 인접 dict
    adjacency_dict = dict()
    for i in range(0, node*2, 2):
        # 인접정보를 100개씩이나 만들고 싶지않아서, 연결된것만 넣기
        # key가 있으면 append, 없으면 값을 지정
        if adjacency_dict.get(node_list[i], -1) == -1:
            adjacency_dict[node_list[i]] = [node_list[i + 1]]
        else:
            adjacency_dict[node_list[i]].append(node_list[i + 1])

    # 출력
    print('#{} {}'.format(tc, IsConnect()))

