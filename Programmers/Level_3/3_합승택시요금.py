from heapq import heappush, heappop

def solution(n, s, a, b, fares):
    # 합승해서 갈 정점을 v라고 하면
    # s~v + v~a + v~b 이걸 각각 구하면 된다. s~v나 v~s나 같으니까
    # v를 시작점으로하는 다익스트라를 모두 구해서 저 3개를 더한 것중 최소를 찾으면 되겠다
    # 그리고 노합승으로 가는 s~b + s~a 최소값이랑 비교하자. 근데 이게 s~s + s~b + s~a랑 같다
    # v가 s인거랑 같음, 그냥 각각으로 시작하는 다익스트라 돌리면 됨

    graph = [[] for _ in range(n+1)]
    for u, v, w in fares:
        graph[u].append((w, v))
        graph[v].append((w, u))

    def Dijkstra(v):
        heap = []
        distance = [987654321] * (n + 1)
        distance[v] = 0
        visit = [0] * (n + 1)
        heappush(heap, (0, v))

        while heap:
            s_to_v, v = heappop(heap)

            if visit[v]:
                continue
            visit[v] = 1

            for v_to_w, w in graph[v]:
                s_to_w = s_to_v + v_to_w
                distance[w] = min(distance[w], s_to_w)
                heappush(heap, (distance[w], w))

        return distance[s] + distance[a] + distance[b]

    min_fee = 987654321
    for i in range(1, n+1):
        min_fee = min(min_fee, Dijkstra(i))

    return min_fee

print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))