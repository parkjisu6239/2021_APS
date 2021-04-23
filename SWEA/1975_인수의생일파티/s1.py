import sys
from heapq import heappush, heappop
sys.stdin = open('input.txt')


def solution(graph, party):
    # 시작점 방문체크
    visit = [0] * (V+1)
    visit[party] = 1

    # 시작점 거리 0
    distance = [987654321] * (V+1)
    distance[party] = 0

    # 힙
    heap = []
    heappush(heap, (0, party))

    while heap:
        party_v_d, v = heappop(heap)

        for v_w, w in graph[v]:
            if visit[w] == 0:
                party_w_d = party_v_d + v_w
                if party_w_d < distance[w]:
                    distance[w] = party_w_d
                    heappush(heap, (party_w_d, w))


    return distance


for tc in range(1, int(input())+1):
    V, E, party = map(int, input().split())
    party_back = [[] for _ in range(V+1)]
    party_go = [[] for _ in range(V+1)]

    for _ in range(E):
        s, e, w = map(int, input().split())
        party_back[s].append((w, e))
        party_go[e].append((w, s))

    back_d = solution(party_back, party)
    go_d = solution(party_go, party)

    max_d = 0
    for i in range(1, V+1):
        max_d = max(max_d, back_d[i] + go_d[i])

    print('#{} {}'.format(tc, max_d))