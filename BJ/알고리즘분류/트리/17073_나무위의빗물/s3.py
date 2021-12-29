import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N, W = map(int, input().split())
tree = [[0] * (N+1) for _ in range(N+1)]
visit = [0] * (N+1)

for _ in range(N-1):
    v, w = map(int, input().split())
    tree[v][w] = 1
    tree[w][v] = 1


def BFS():
    result = 0
    cnt = 0
    que = [(1, W)]
    visit[1] = 1

    while que:
        v, water = que.pop(0)
        child = 0

        for w in range(1, N+1):
            if visit[w]:
                continue

            if tree[v][w] == 0:
                continue

            visit[w] = 1
            que.append((w, water/2))
            child += 1

        if child == 0:
            result += water
            cnt += 1

    return result / cnt


print(BFS())