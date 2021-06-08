import sys
from heapq import heappush, heappop
sys.stdin = open('eval_input.txt')

# 힙_프림 #
'''
프림은 경로 자체와 가장 가까이 있는 정점을 택하는 것
1. 처음 시작점은 0 or 1, 가중치 0으로 힙에 넣고 시작
2. 시작점과 연결된것 중 방문하지 않은 것 모두 힙에 추가
3. 위에서 추가한 정점중 가중치가 가장 작은 것으로 2번 재실행
4. 그러면 힙에 있는 값들은 (어딘가와 v의 거리, v) 이런식으로 저장된다.
5. 저 어딘가가 어디인지에 관계 없이, 작은 값을 택한다. (방문하지 않은 경우)
ㄴ 어느정점과 인접인지는 상관없다. 힙에 들어왔다는건 방문체크된 최소신장트리의 정점 중 하나와는 반드시 연결되어있기 때문.

'''
V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]

for i in range(E): # 인접정점인 경우 graph 갱신
    s, e, w = map(int, input().split())
    graph[s].append((w, e))
    graph[e].append((w, s))

visit = [0]*(V+1)
node = 0

heap = []
heappush(heap, (0, 1))

result = 0

while node < V:
    # path_to_v : 최소신장트리(경로)~v와의 거리 (선과 점의 거리랄까..?)
    path_to_v, v = heappop(heap) # 가장 가까운 값 추출

    if visit[v]: # 방문했으면 버리기 -> 이전에 더 가까운 거리로 연결한 것
        continue

    visit[v] = 1 # 방문체크
    node += 1 # 연결노드수 + 1
    result += path_to_v # 최소신장트리 가중치 추가

    for direct_v_w, w in graph[v]: # v의 인접정점 중에서
        if visit[w] == 0: # 방문하지 않은 정점에 대하여
            heappush(heap, (direct_v_w, w)) # v-w거리, w 추가


print(result)





