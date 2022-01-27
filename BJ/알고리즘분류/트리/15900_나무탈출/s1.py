import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
adj = [[0] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)

for __ in range(N-1):
    a, b = map(int, input().split())
    adj[a][b] = 1
    adj[b][a] = 1


que = [(1, 0)]
visited[1] = 1
result = 0

while que:
    v, d = que.pop(0)

    is_leaf = True

    for w in range(1, N+1):
        if adj[v][w] == 0:
            continue

        if visited[w]:
            continue

        visited[w] = 1

        is_leaf = False
        que.append((w, d+1))

    if is_leaf:
        result += d

print("Yes" if result % 2 else "No")

