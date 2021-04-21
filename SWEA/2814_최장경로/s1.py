import sys
sys.stdin = open('input.txt')


def DFS(v, cnt):
    global max_d

    visit[v] = 1

    for w in graph[v]:
        if visit[w] == 0:
            visit[w] = 1
            DFS(w, cnt+1)
            max_d = max(max_d, cnt + 1) # 함수빠져나왔을때가, 그 정점에서의 최장
            visit[w] = 0



for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        v, w = map(int, input().split())
        graph[v].append(w)
        graph[w].append(v)

    max_d = 1 # 최소경로

    for i in range(1, V+1): # 모든정점에서 시작해봐야함
        visit = [0] * (V + 1)
        visit[i] = 1
        DFS(i, 1)

    print('#{} {}'.format(tc, max_d))
