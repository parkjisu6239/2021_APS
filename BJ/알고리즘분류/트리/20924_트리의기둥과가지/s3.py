import sys

sys.setrecursionlimit(2500)

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


def get_longest_branch():
    global longest

    temp = []
    for leaf in range(1, N+1):
        if leaf == root:
            continue

        if len(nodes[leaf]) == 1:
            temp.append(leaf)

    for l in temp:
        v = l
        branch = 0
        while v != giga:
            branch += nodes[v][0][1]
            v = nodes[v][0][0]
        longest = max(longest, branch)


if N == 1:
    print(0, 0)
else:
    giga, column = get_giga_node()
    longest = 0
    get_longest_branch()
    print(column, longest)
