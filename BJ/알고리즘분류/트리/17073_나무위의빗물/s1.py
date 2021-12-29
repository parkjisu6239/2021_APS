import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N, W = map(int, input().split())
tree = [[] for _ in range(N+1)]
visit = [0] * (N+1)

for _ in range(N-1):
    v, w = map(int, input().split())
    tree[v].append(w)
    tree[w].append(v)


def BFS():
    result = []
    que = [(1, W)]
    visit[1] = 1

    while que:
        v, water = que.pop(0)
        child = 0

        for w in tree[v]:
            if visit[w]:
                continue

            visit[w] = 1
            que.append((w, water/2))
            child += 1

        if child == 0:
            result.append(water)

    return sum(result)/len(result)


print(BFS())