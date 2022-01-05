import sys

sys.setrecursionlimit(1000000)

sys.stdin = open('input.txt')
input = sys.stdin.readline

N, root = map(int, input().split())
nodes = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(N-1):
    a, b, d = map(int, input().split())
    nodes[a].append((b, d))
    nodes[b].append((a, d))


def get_giga_node():
    column = 0
    giga = root
    visited[giga] = 1

    # root가 아닌데 인접노드가 2개보다 많으면, 자식이 두개 -> giga
    # root인데, 인접노드가 2개 이상이면, 자식이 두개 -> giga
    while not(len(nodes[giga]) > 2 or (len(nodes[giga]) > 1 and giga == root)):
        if giga != root and len(nodes[giga]) == 1: # giga가 leap인 경우
            break

        for w, d in nodes[giga]:
            if w == giga:
                continue

            if visited[w]:
                continue

            column += d
            giga = w
            visited[giga] = 1
            break

    return giga, column


def dfs(v, branch_len):
    global longest

    if len(nodes[v]) == 1:
        longest = max(longest, branch_len)
        return

    for w, d in nodes[v]:
        if w == v:
            continue

        if visited[w]:
            continue

        visited[v] = 1
        dfs(w, branch_len + d)
        visited[v] = 0


if N == 1:
    print(0, 0)
else:
    giga, column = get_giga_node()
    longest = 0
    dfs(giga, 0)
    print(column, longest)
