import sys
sys.stdin = open('input.txt')

# 시간초과남, 힙 써보기

def springAndSummer():
    for r in range(N):
        for c in range(N):
            if not trees[r][c]: continue

            # spring
            dead = -1
            for i in range(len(trees[r][c])):
                if trees[r][c][i] <= land[r][c]: # 나무 나이 < 양분
                    land[r][c] -= trees[r][c][i]
                    trees[r][c][i] += 1
                else:
                    dead = i # 나무 나이 > 양분
                    break # 그 뒤에 있는 나무들 다이

            # summer
            add = 0
            if dead != -1:
                for j in  range(dead, len(trees[r][c])):
                    add += trees[r][c][j] // 2
                trees[r][c] = trees[r][c][:dead]

            trees[r][c].sort()
            land[r][c] += add


def fall():
    for r in range(N):
        for c in range(N):

            if not trees[r][c]: continue

            for i in range(len(trees[r][c])):
                if trees[r][c][i] % 5: continue

                # 나이가 5의 배수
                for k in range(8):
                    nr, nc = r + dr[k], c + dc[k]
                    if 0 <= nr < N and 0 <= nc < N:
                        trees[nr][nc].insert(0, 1) # 나이가 1인 나무 맨 앞에 추가


def winter():
    for r in range(N):
        for c in range(N):
            land[r][c] += A[r][c]


def solution():
    # K년 후...
    for _ in range(K):
        springAndSummer()
        fall()
        winter()

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
    trees[x-1][y-1].append(z)

for r in range(N):
    for c in range(N):
        trees[r][c].sort() # 어린 나무 순서로 배치


solution()