import sys
sys.stdin = open('input.txt')

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
visit = dict()


for i in range(1, R-1):
    for j in range(1, C-1):
        if arr[i][j] == 'R':
            red_r, red_c = i, j
        if arr[i][j] == 'B':
            blue_r, blue_c = i, j
        if arr[i][j] == 'O':
            goal_r, goal_c = i, j


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


que = [(red_r, red_c, blue_r, blue_c, 1)]

end = False

while not end and que:

    red_r, red_c, blue_r, blue_c, cnt = que.pop(0)

    if cnt > 10:
        break

    if visit.get((red_r, red_c, blue_r, blue_c), 0):
        continue

    visit[(red_r, red_c, blue_r, blue_c)] = 1

    for d in range(4):
        red_hole, blue_hole = False, False
        nrr, nrc = red_r + dr[d], red_c + dc[d]

        while arr[nrr][nrc] != "#":
            if arr[nrr][nrc] == 'O':
                red_hole = True
                break
            nrr += dr[d]
            nrc += dc[d]

        nrr -= dr[d]
        nrc -= dc[d]

        nbr, nbc = blue_r + dr[d], blue_c + dc[d]
        while arr[nbr][nbc] != "#":
            if arr[nbr][nbc] == 'O':
                blue_hole = True
                break
            nbr += dr[d]
            nbc += dc[d]

        nbr -= dr[d]
        nbc -= dc[d]

        if red_hole and not blue_hole:
            end = True
            break

        if blue_hole:
            continue

        if(nrr, nrc) == (nbr, nbc):
            if d == 0:
                if red_r > blue_r:
                    nrr += 1
                else:
                    nbr += 1
            elif d == 1:
                if red_r < blue_r:
                    nrr -= 1
                else:
                    nbr -= 1
            elif d == 2:
                if red_c > blue_c:
                    nrc += 1
                else:
                    nbc += 1
            else:
                if red_c < blue_c:
                    nrc -= 1
                else:
                    nbc -= 1

        que.append((nrr, nrc, nbr, nbc, cnt + 1))

if end:
    print(cnt)
else:
    print(-1)

