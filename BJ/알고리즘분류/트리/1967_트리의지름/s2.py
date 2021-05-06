import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

V = int(input())
tree = [[] for _ in range(V+1)]
# 원의 중심은 가장 먼 두 노드의 공통 조상
info = [[0, 0] for _ in range(V+1)]

for _ in range(V-1):
    p, c, w = map(int, input().split())
    tree[p].append([c, w])

def post_order(v):
    if v <= V and tree[v]:
        a = post_order(v*2)
        b = post_order(v * 2 + 1)
        info[v][0] = max(a, b)
        info[v][1] = a + b

print(tree)
post_order(1)
