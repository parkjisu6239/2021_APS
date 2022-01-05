import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N, root = map(int, input().split())
nodes = [[0] * (N+1) for _ in range(N+1)]
connect_cnt = [0] * (N+1) # 인접한 노드 수
visited = [0] * (N+1)

for _ in range(N-1):
    a, b, d = map(int, input().split())
    nodes[a][b] = d
    nodes[b][a] = d
    connect_cnt[a] += 1
    connect_cnt[b] += 1


def get_giga_node():
    column = 0
    giga = root
    visited[giga] = 1

    # root가 아닌데 인접노드가 2개보다 많으면, 자식이 두개 -> giga
    # root인데, 인접노드가 2개 이상이면, 자식이 두개 -> giga
    while not(connect_cnt[giga] > 2 or (connect_cnt[giga] > 1 and giga == root)):
        if giga != root and connect_cnt[giga] == 1: # giga가 leap인 경우
            break

        for w in range(1, N+1):
            if w == giga:
                continue

            if visited[w]:
                continue

            if nodes[giga][w]:
                column += nodes[giga][w]
                giga = w
                visited[giga] = 1
                break

    return giga, column


def dfs(v, branch_len):
    global longest

    if connect_cnt[v] == 1:
        longest = max(longest, branch_len)
        return

    for w in range(1, N+1):
        if w == v:
            continue

        if visited[w]:
            continue

        if nodes[v][w]:
            visited[v] = 1
            dfs(w, branch_len + nodes[v][w])
            visited[v] = 0


def solution():
    if N == 1:
        return 0, 0

    giga, column = get_giga_node()
    longest = 0
    dfs(giga, 0)
    return column, longest


print(*solution())