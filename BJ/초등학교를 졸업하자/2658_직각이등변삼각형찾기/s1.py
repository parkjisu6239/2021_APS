import sys

sys.stdin = open('input4.txt')
input = sys.stdin.readline

arr = [list(map(int, input().rstrip())) for _ in range(10)]

direc = [(1, -1), (1, 0), (1, 1), (0, 1)]


def get_point(x, y, dx, dy):
    nx, ny = x + dx, y + dy
    while 0 <= nx < 10 and 0 <= ny < 10 and arr[nx][ny]:
        nx += dx
        ny += dy
    return nx - dx, ny - dy


def get_all_point():
    points = []
    for x in range(10):
        for y in range(10):
            if arr[x][y]:
                points.append((x, y))
                for dx, dy in direc:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx > 9 or ny < 0 or ny > 9:
                        continue
                    if arr[x + dx][y + dy]:
                        points.append(get_point(x, y, dx, dy))

                return points


def solution():
    points = get_all_point()
    if len(points) < 3 or len(points) > 4:
        print(0)
        return

    dist = []
    for i in range(1, len(points)):
        d = (points[i][0] - points[0][0]) ** 2 + (points[i][1] - points[0][1]) ** 2
        dist.append(d)

    if len(points) == 4:
        H = dist.index(min(dist))
        del points[H+1]
        del dist[H]

    dist.append((points[1][0] - points[2][0]) ** 2 + (points[1][1] - points[2][1]) ** 2)
    dist.sort()

    if dist[0] + dist[1] == dist[2]:
        points.sort()
        for x, y in points:
            print(x+1, y+1)
        return

    print(0)



solution()

