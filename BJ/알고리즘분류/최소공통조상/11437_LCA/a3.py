import sys
sys.stdin = open('input.txt')

from collections import defaultdict as dd
input = sys.stdin.readline
sys.setrecursionlimit(70000)
n = int(input())
maxn = 65536
connected = [[] for _ in range(n+10)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    connected[a].append(b)
    connected[b].append(a)
m = int(input())
pairset = dd(list)
ans_order = []
for _ in range(m):
    a, b = map(int, input().split())
    pairset[a].append(b)
    pairset[b].append(a)
    ans_order.append(a * maxn + b if a < b else b * maxn + a)
parent = {}
visited = [False] * (n+10)
ans = {}
def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    parent[find(y)] = find(x)

def LCA(start):
    parent[start] = start
    for child in connected[start]:
        if child in parent:
            continue
        LCA(child)
        union(start, child)
    visited[start] = True
    for other in pairset[start]:
        if visited[other]:
            k = start * maxn + other if start < other else other * maxn + start
            ans[k] = find(other)

LCA(1)
for i in ans_order:
    print(ans[i])