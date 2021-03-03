import sys
sys.stdin = open('input.txt')

def IsConnect(adjacency_list):
    # DFS를 위한 변수 생성
    visited = [ 0 for _ in range(100)]
    stack = [0]

    # stack에 값이 있다면 반복
    while stack:
        if visited[99]:
            return 1

        # 방문했다면
        if visited[stack[-1]]:
            stack.pop()
        # 방문하지 않았다면
        else:
            # 방문체크 하고 빼기
            v =  stack[-1]
            visited[v] = 1
            stack.pop()

            # 현재 정점에서 갈 수 있는 곳중에
            for connect in adjacency_list[v]:
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

    # 인접 리스트 생성
    adjacency_list = [[] for _ in range(100)]
    for i in range(0, node*2, 2):
        adjacency_list[node_list[i]].append(node_list[i+1])

    # 출력
    print('#{} {}'.format(tc, IsConnect(adjacency_list)))

