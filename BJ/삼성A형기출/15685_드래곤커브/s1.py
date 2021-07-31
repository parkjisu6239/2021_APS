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
    directions = [d]
    land[r][c] = 1

    for _ in range(g):
        temp = []
        for i in range(len(directions)):
            direc = directions[-i -1] # 뒤에서 부터
            ro_direc = (direc - 3) % 4
            temp.append(ro_direc)

        directions.extend(temp)

    for k in directions:
        nr, nc = r + dr[k], c + dc[k]
        land[nr][nc] = 1
        r, c = nr, nc



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
dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

for _ in range(N):
    x, y, d, g = map(int, sys.stdin.readline().split())
    setDrangonCurve(y, x, d, g)
print(countSquare())