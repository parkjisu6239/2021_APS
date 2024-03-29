import sys
sys.setrecursionlimit(10**9)

sys.stdin = open('input.txt')
input = sys.stdin.readline

N, R, Q = map(int, input().split())
tree = [[] for _ in range(N+1)]
children = [[] for _ in range(N + 1)]
size = [0] * (N+1)

for _ in range(N-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)


def makeTree(cur, parent):
    for child in tree[cur]:
        if child == parent:
            continue
        children[cur].append(child)
        makeTree(child, cur)


def getSize(cur):
    size[cur] = 1
    for child in children[cur]:
        getSize(child)
        size[cur] += size[child]


makeTree(R, -1)
getSize(R)

for i in range(Q):
    q = int(input())
    print(size[q])

