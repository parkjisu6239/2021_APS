import sys
from heapq import heappop, heappush
sys.stdin = open('input.txt')

for _ in range(int(input())):

    V, E, hack = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        s, e, w = map(int, input().split()) # e -> s (감염이 퍼진다)
        graph[e].append((w, s)) # 가중치, 시작점

    distance = [999999] * (V+1) # 초기시간은 무한
    heap = [] # 힙 사용
    heappush(heap, (0, hack)) # 시작은 0초, 감염원
    distance[hack] = 0

    while heap:
        # hack~v까지 가중치, v번 컴퓨터
        from_hack_to_v, v = heappop(heap) # 가중치가 작은 것부터 나온다.

        if distance[v] < from_hack_to_v: # 이전에 저장된 시간이 더 짧으면 넘기기
            continue

        for direct_vw, w in graph[v]:
            new_d = from_hack_to_v + direct_vw
            if new_d < distance[w]:
                distance[w] = new_d
                heappush(heap, (new_d, w))


    last_time = 0
    time = 0
    for d in distance:
        if d != 999999:
            if time < d:
                time = d
            last_time += 1

    print(last_time, time)








