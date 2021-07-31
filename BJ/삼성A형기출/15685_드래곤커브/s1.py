# 우
# (우 90도) 하 -> 상
# (우상 90도) 하 우 -> 좌 상
# (우상좌상 90도) 하 우 상 우 -> 좌 하 좌 상
# 하 우 상 우 상 좌 상 우 -> 좌 하 우 하 좌 하 좌 상

# 90도 회전 방향 우 -> 하 -> 좌 -> 상 -> 우
# 드래곤 커브의 n세대는 n-1 세대의 누적 이동 방향을 90도 회전 한 후
# 이를 n-1 세대의 꼬리부터 역방향으로 반대로 배치하는 것

import sys
sys.stdin = open('input.txt')


def setDrangonCurve(r, c, d, g):
    directions = []
    land[r][c] = 1
    gener = 0

    while gener <= g:
        if gener == 0:
            dr, dc = move[d]
            r, c = r + dr, c + dc
            land[r][c] = 1

            directions.append(d)
            gener += 1
            continue

        temp = []
        for i in range(len(directions)):
            direc = directions[len(directions) - i - 1] # 뒤에서 부터
            ro_direc = (direc - 3) % 4
            dr, dc = move[ro_direc]
            r, c = r + dr, c + dc
            land[r][c] = 1
            temp.append(ro_direc)

        gener += 1
        directions.extend(temp)


def countSquare():
    cnt = 0
    for i in range(99):
        for j in range(99):
            if land[i][j] == 0: continue

            if land[i+1][j] and land[i][j+1] and land[i+1][j+1]:
                cnt += 1

    return cnt



N = int(input())
land = [[0] * 101 for _ in range(101)]
move = {0: (0, 1), 1: (-1, 0), 2: (0, -1), 3: (1, 0)}

for _ in range(N):
    x, y, d, g = map(int, sys.stdin.readline().split())
    setDrangonCurve(y, x, d, g)
print(countSquare())