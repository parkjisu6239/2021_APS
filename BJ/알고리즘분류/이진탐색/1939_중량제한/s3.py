import sys
from collections import defaultdict
from heapq import heappop, heappush

sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
bridge = defaultdict(dict)
upper = 0
for _ in range(M):
    A, B, C = map(int, input().split())
    upper = max(upper, C)
    bridge[A][B] = max(bridge[A].get(B, 0), C)
    bridge[B][A] = max(bridge[B].get(A, 0), C)
start, end = map(int, input().split())


def bfs(start, limit):
    que = [(-1000000000, start)]
    visited = [0] * (N + 1)
    while que:
        min_val, v = heappop(que)
        if visited[v]:
            continue

        visited[v] = 1

        if v == end:
            return -min_val

        for w, weight in bridge[v].items():
            if visited[w]:
                continue
            if weight < limit:
                continue
            heappush(que, (-min(-min_val, weight), w))

    return 0


def bs(l, r):
    if l > r:
        return r

    m = (l + r) // 2
    value = bfs(start, m)
    if value:
        return bs(max(value, m)+1, r)
    else:
        return bs(l, m-1)


print(bs(1, upper))
