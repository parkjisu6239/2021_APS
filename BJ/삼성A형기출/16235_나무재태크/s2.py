import sys
from heapq import heappop, heappush
sys.stdin = open('input.txt')
input = sys.stdin.readline


def springAndSummer():
    for r in range(N):
        for c in range(N):
            if not trees[r][c]: continue

            # spring
            add = 0
            temp = []
            while trees[r][c]:
                tree = heappop(trees[r][c])
                if tree <= land[r][c]: # 나무 나이 < 양분
                    land[r][c] -= tree
                    tree += 1
                    heappush(temp, tree)
                else:
                    # summer
                    add += tree // 2

            trees[r][c] = temp
            land[r][c] += add


def fallAndWinter():
    for r in range(N):
        for c in range(N):

            # fall
            if not trees[r][c]:
                land[r][c] += A[r][c]
                continue

            for i in range(len(trees[r][c])):
                if trees[r][c][i] % 5: continue

                # 나이가 5의 배수
                for k in range(8):
                    nr, nc = r + dr[k], c + dc[k]
                    if 0 <= nr < N and 0 <= nc < N:
                        trees[nr][nc].insert(0, 1) # 나이가 1인 나무 맨 앞에 추가

            # winter
            land[r][c] += A[r][c]


def solution():
    # K년 후...
    for _ in range(K):
        springAndSummer()
        fallAndWinter()

    surviver = 0
    for r in range(N):
        for c in range(N):
            surviver += len(trees[r][c])
    print(surviver)


N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
trees = [[[] for _ in range(N)] for __ in range(N)]
land = [[5 for _ in range(N)] for ___ in range(N)]

dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

for _ in range(M):
    x, y, z = map(int, input().split())
    heappush(trees[x-1][y-1], z)

solution()