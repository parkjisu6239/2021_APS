import sys
sys.stdin = open('input.txt')

from heapq import heappop, heappush
'''
다익스트라에서는 1 -> 2 (5) 보다 1 -> 3 -> 4 -> 5 -> 2 (4) 가 더 최소비용인 경로일 수 있다.
힙을 사용하면 1 -> 2가 힙에 먼저 들어올 수는 있지만, 먼저 나가는건 3->4->5->2 일 것이다. (각 가중치 1이라 할때)
그래서 항상 특정 경로로 가는 최소 거리가 먼저 작성 된다.
'''
for _ in range(int(input())):
    V, E, hack = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        s, e, w = map(int, input().split()) # e -> s (감염이 퍼진다)
        graph[e].append((w, s)) # 가중치, 시작점

    distance = [987654321] * (V+1) # 초기시간은 무한
    distance[hack] = 0

    heap = [] # 힙 사용
    heappush(heap, (0, hack)) # 시작은 0초, 감염원

    while heap:
        # hack~v까지 가중치, v번 컴퓨터
        from_hack_to_v, v = heappop(heap) # 가중치가 작은 것부터 나온다.

        if distance[v] < from_hack_to_v: # 이전에 저장된 시간이 더 짧으면 넘기기
            continue # 위 설명처럼 1->2가 힙에 남아있지만, 1->3->4->5->2로 2의 distance가 4로 저장된 상태라면 넘기는 것

        for direct_vw, w in graph[v]:
            new_d = from_hack_to_v + direct_vw # 감염원~v + v-w = 감염원~w (새로운 경로)
            if new_d < distance[w]:
                distance[w] = new_d
                heappush(heap, (new_d, w))
                # 힙에 들어가는 건 감염원~w의 거리(바로 가는거,, 거쳐 가는거,, 등등 다 들어감 , 방문하기 전까지는)


    infection = 0
    time = 0
    for d in distance:
        if d != 987654321:
            infection += 1
            time = max(time, d)


    print(infection, time)
    print(distance)








