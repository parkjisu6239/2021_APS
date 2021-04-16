import sys
sys.stdin = open('input.txt')


for tc in range(1, int(input())+1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    visit = [0] * (N*N+1)

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for r in range(N):
        for c in range(N):
            for i in range(4):
                if 0 <= r+dr[i] < N and 0 <= c+dc[i] < N and room[r][c]+1 == room[r+dr[i]][c+dc[i]]:
                    visit[room[r][c]] = 1

    start = 0
    max_move = 0
    i = 1
    while i < len(visit):
        if visit[i] == 1:
            long = 2
            for j in range(i+1, len(visit)):
                if visit[j] == 1:
                    long += 1
                else:
                    if long > max_move:
                        max_move = long
                        start = i
                    i = j
                    break
        i += 1

    print('#{} {} {}'.format(tc, start, max_move))