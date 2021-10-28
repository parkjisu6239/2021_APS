import sys
sys.stdin = open('input.txt')
input = lambda : map(int, sys.stdin.readline().split())

N, K = input()
arr = [list(input()) for _ in range(N)]
player = [[[] for _ in range(N)] for _ in range(N)]
player_info = []

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]
change = [1, 0, 3, 2]

for i in range(K):
    r, c, d = input()
    player[r-1][c-1].append(i)
    player_info.append([r-1, c-1, d])


def play(idx):
    r, c, d = player_info[idx]

    group = player[r][c][player[r][c].index(idx):]
    player[r][c] = player[r][c][:player[r][c].index(idx)]

    if not(0 <= r + dr[d] < N and 0 <= c + dc[d] < N): # 이동시 밖으로 나가는 경우
        # 방향 바꿔서
        for i, gr, gc, gd in enumerate(group):
            gd = change[gd]
            gr = r + dr[d]







play(1)