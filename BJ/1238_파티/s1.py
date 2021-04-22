import sys
sys.stdin = open('input.txt')


def go_back(go_back):
    graph = go_back

    distance = [987654] * (V + 1)  # 초기값 무한
    distance[party] = 0  # 자기자신과의 거리 0
    q = [party]

    while q:
        v = q.pop(0)
        for w in range(len(graph[v])):  # 인접 정점중에서
            if distance[v] + graph[v][w] < distance[w]:  # 경유지로 가는게 더 짧다면
                distance[w] = distance[v] + graph[v][w]  # 거리 갱신
                q.append(w)

    return distance


# 1. 각 정점 -> X 시간 : ???
# 2. X -> 각 정점 시간 : v에서 시작하는 다익스트라
# 단방향이라서 시간이 다를 수 있다.

V, E, party = map(int, input().split())
graph_back = [[987654] * (V+1) for _ in range(V+1)] # 초기값 무한
graph_go = [[987654] * (V+1) for _ in range(V+1)] # 초기값 무한

# 1번을 진짜 각 정점에서 시작하게 하면 굉장히 까다롭다.
# 1번은 입력값의 방향을 반대로 생각하여 v에서 출발하는 것으로 생각하는 것과 같다.

for i in range(E): # 인접정점인 경우 graph 갱신
    s, e, w = map(int, input().split())
    graph_back[s][e] = w
    graph_go[e][s] = w


go = go_back(graph_go) # v로 가는데 걸리는 최소 시간
back = go_back(graph_back) # v에서 원래 정점으로 돌아오는데 걸리는 최소 시간


min_d = 0
for i in range(1, V+1):
    d = go[i] + back[i]
    if d > min_d:
        min_d = d

print(min_d)







