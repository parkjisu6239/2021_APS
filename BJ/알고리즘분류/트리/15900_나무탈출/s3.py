import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
adj = [[] for _ in range(N+1)]

for __ in range(N-1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)


def get_leafs():
    temp = []
    for i in range(2, N+1):
        if len(adj[i]) == 1:
            temp.append(i)
    return temp


def get_parent():
    temp = [0] * (N + 1)
    temp[1] = 1
    que = [1]
    while que:
        v = que.pop(0)
        for w in adj[v]:
            if temp[w]:
                continue
            temp[w] = v
            que.append(w)
    return temp


leafs = get_leafs()
parent = get_parent()
result = 0

for leaf in leafs:
    while parent[leaf] != leaf:
        leaf = parent[leaf]
        result += 1

print("Yes" if result % 2 else "No")
