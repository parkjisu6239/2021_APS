import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
arr = [[0] * (N+1) for _ in range(N+1)]


while True:
    v, w = map(int, input().split())
    if v == -1 and w == -1:
        break

    arr[v][w] = 1
    arr[w][v] = 1


def solution():
    ans = [0] * (N+1)
    for v in range(1, N+1):
        ans[v] = dijkstra(v)

    score = min(ans[1:])
    candi = []
    for k in range(1, N+1):
        if ans[k] == score:
            candi.append(k)

    print(score, len(candi))
    print(*candi)


def dijkstra(node):
    visited = [-1] * (N+1)
    visited[node] = 0
    que = [(node, 0)]

    while que:
        v, d = que.pop(0)

        for w in range(1, N+1):
            if visited[w] != -1:
                continue

            if arr[v][w]:
                visited[w] = d + 1
                que.append((w, d+1))

    return max(visited)

solution()