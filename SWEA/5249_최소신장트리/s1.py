import sys
sys.stdin = open('input.txt')

# 크루스컬 #

def find_set(x): # 루트 노드 찾기
    if x != p[x]:
        return find_set(p[x])
    else:
        return x


def union(x, y): # 루트 노드 잇기
    p[find_set(y)] = find_set(x) # y의 루트를 x의 루트로 지정



for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    graph = [[0] * (V+1) for _ in range(V+1)] # 0~V
    edges = [] # 간선정보

    for i in range(E): # 인접행렬
        s, e, w = map(int, input().split())
        graph[s][e] = w
        graph[e][s] = w
        edges.append([s, e, w])

    # 가중치 오름차순
    edges.sort(key = lambda x : (x[2]))

    # 부모정보 초기화
    p = list(range(V+1))

    connect_E = 0 # 연결한 엣지 수
    min_cost = 0 # 최소 가중치

    i = 0
    while connect_E < V:
        s, e, w = edges[i]

        if find_set(s) != find_set(e): # 루트노드가 다르면
            union(s, e)
            connect_E += 1
            min_cost += w

        i += 1

    print('#{} {}'.format(tc, min_cost))


