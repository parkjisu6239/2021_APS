import sys
from heapq import heappop, heappush

sys.stdin = open('input.txt')
input = sys.stdin.readline

R, C = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(R)]
visited = [[[20, 20] for _ in range(C)] for __ in range(R)]

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
dir = ['D', 'R', 'U', 'L']


def is_can_move(r, c):
    if arr[r][c] == '#':
        return False
    else:
        return True


def get_next_pos(dir_pk, cur_r, cur_c):
    nxt_r, nxt_c = cur_r + dr[dir_pk], cur_c + dc[dir_pk]
    while is_can_move(nxt_r, nxt_c):
        if arr[nxt_r][nxt_c] == 'O':
            return nxt_r, nxt_c

        nxt_r += dr[dir_pk]
        nxt_c += dc[dir_pk]

    return nxt_r - dr[dir_pk], nxt_c - dc[dir_pk]


def get_init_pos():
    red_r, red_c, blue_r, blue_c = -1, -1, -1, -1
    for r in range(R):
        for c in range(C):
            if arr[r][c] == 'R':
                red_r = r
                red_c = c
            elif arr[r][c] == 'B':
                blue_r = r
                blue_c = c

            if red_r != -1 and red_c != -1 and blue_r != -1 and blue_c != -1:
                return red_r, red_c, blue_r, blue_c


def back_ball(dir_pk, red, blue, cur):
    if dir_pk == 0:
        if red[0] > blue[0]:
            return cur[0], cur[1], cur[0] -1, cur[1]
        else:
            return cur[0]-1, cur[1], cur[0], cur[1]
    elif dir_pk == 2:
        if red[0] > blue[0]:
            return cur[0]+1, cur[1], cur[0], cur[1]
        else:
            return cur[0], cur[1], cur[0]+1, cur[1]
    elif dir_pk == 1:
        if red[1] > blue[1]:
            return cur[0], cur[1], cur[0], cur[1]-1
        else:
            return cur[0], cur[1]-1, cur[0], cur[1]
    else:
        if red[1] > blue[1]:
            return cur[0], cur[1]+1, cur[0], cur[1]
        else:
            return cur[0], cur[1], cur[0], cur[1]+1


def bfs():
    heap = [(0, '', *get_init_pos())]
    while heap:
        cnt, path, red_r, red_c, blue_r, blue_c = heappop(heap)
        if cnt >= visited[red_r][red_c][0] and cnt >= visited[blue_r][blue_c][1]:
            continue
        visited[red_r][red_c][0] = cnt
        visited[blue_r][blue_c][1] = cnt

        if cnt > 10:
            continue

        for k in range(4):
            nxt_red_r, nxt_red_c = get_next_pos(k, red_r, red_c)
            nxt_blue_r, nxt_blue_c = get_next_pos(k, blue_r, blue_c)

            if arr[nxt_red_r][nxt_red_c] == 'O':
                if arr[nxt_blue_r][nxt_blue_c] != 'O':
                    return [cnt + 1, path + dir[k]]
                else:
                    continue

            if (nxt_red_r, nxt_red_c) == (nxt_blue_r, nxt_blue_c):
                nxt_red_r, nxt_red_c, nxt_blue_r, nxt_blue_c = back_ball(k, [red_r, red_c], [blue_r, blue_c], [nxt_red_r, nxt_red_c])

            if (nxt_red_r, nxt_red_c) == (red_r, red_c) and (nxt_blue_r, nxt_blue_c) == (blue_r, blue_c):
                continue

            heappush(heap, (cnt+1, path + dir[k], nxt_red_r, nxt_red_c, nxt_blue_r, nxt_blue_c))

    return [-1]


for i in bfs():
    print(i)
