import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
visit = [[0]*N for _ in range(M)]
dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]


def solution():
    rooms = get_room()
    biggest = get_break_wall_biggest_room(rooms)

    print(len(rooms))
    print(max(rooms))
    print(biggest)


def get_room():
    rooms = []
    room_idx = 1
    for r in range(M):
        for c in range(N):
            if visit[r][c] == 0:
                rooms.append(bfs(r, c, room_idx))
                room_idx += 1

    return rooms


def get_break_wall_biggest_room(rooms):
    biggest = 0
    for r in range(M):
        for c in range(N):
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < M and 0 <= nc < N and visit[r][c] != visit[nr][nc]:
                    biggest = max(biggest, rooms[visit[r][c]-1] + rooms[visit[nr][nc]-1])

    return biggest


def bfs(r, c, room_idx):
    que = [(r, c)]
    visit[r][c] = room_idx
    width = 1

    while que:
        r, c = que.pop()
        for i in range(4):
            if arr[r][c] & (1 << i):
                continue
            nr, nc = r + dr[i], c + dc[i]
            if not visit[nr][nc]:
                visit[nr][nc] = room_idx
                que.append((nr, nc))
                width += 1

    return width

solution()