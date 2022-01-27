import sys

sys.setrecursionlimit(10**5)
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
adj = [[] for _ in range(N+1)]
result = 0

for __ in range(N-1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)


def dfs(v, d, prev):
    global result
    if v != 1 and len(adj[v]) == 1:
        result += d
        return

    for w in adj[v]:
        if w == prev:
            continue

        dfs(w, d+1, v)


dfs(1, 0, 0)


print("Yes" if result % 2 else "No")

