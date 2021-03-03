import sys
sys.stdin = open('input.txt')

def IsConnect():
    # DFS를 위한 변수 생성
    visited = []
    stack = [0]
    visited.append(0)

    # stack에 값이 있다면 반복
    while stack:
        # 목표지점에 방문했으면 1로 종료
        if 99 in visited:
            return 1

        # 방문체크 하고 빼기
        v =  stack[-1]
        visited.append(v)
        stack.pop()

        # 현재 정점에서 갈 수 있는 곳중에
        if adjacency_dict.get(v, -1) != -1:
            for connect in adjacency_dict[v]:
                # 방문하지 않은 곳을 스택에 쌓기
                if connect not in visited:
                    stack.append(connect)
                    visited.append(connect)

    if 99 in visited:
        return 1
    else:
        return 0



for _ in range(10):
    # 입력
    tc, node = map(int, input().split())
    node_list = list(map(int, input().split()))

    # 인접 리스트 생성
    adjacency_dict = dict()
    for i in range(0, node*2, 2):
        # key가 있으면 append, 없으면 값을 지정
        if adjacency_dict.get(node_list[i], -1) == -1:
            adjacency_dict[node_list[i]] = [node_list[i + 1]]
        else:
            adjacency_dict[node_list[i]].append(node_list[i + 1])

    # 출력
    print('#{} {}'.format(tc, IsConnect()))

