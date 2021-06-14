import sys
sys.stdin = open('input.txt')

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
visit = [[[[0] * C for _ in range(R)] for __ in range(C) ] for ___ in range(R)]


for i in range(1, R-1):
    for j in range(1, C-1):
        if arr[i][j] == 'R':
            red = (i, j)
        if arr[i][j] == 'B':
            blue = (i, j)
        if arr[i][j] == 'O':
            goal = (i, j)


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

result = []

def solution(red, blue, cnt):

    if blue == goal or cnt > 10:
        result.append(cnt)
        return -1

    if red == goal:
        result.append(cnt)
        return

    if visit[red[0]][red[1]][blue[0]][blue[1]]:
        return

    visit[red[0]][red[1]][blue[0]][blue[1]] = 1

    rr, rc = red
    br, bc = blue
    for d in range(4):
        nrr, nrc = rr + dr[d], rc + dc[d]
        while arr[nrr][nrc] != "#":
            nrr += dr[d]
            nrc += dc[d]

        nrr -= dr[d]
        nrc -= dc[d]

        nbr, nbc = br + dr[d], bc + dc[d]
        while arr[nbr][nbc] != "#":
            nbr += dr[d]
            nbc += dc[d]

        nbr -= dr[d]
        nbc -= dc[d]

        if(nrr, nrc) == (nbr, nbc):
            if d == 0:
                if rr > br:
                    nrr += 1
                else:
                    nbr += 1
            elif d == 1:
                if rr < br:
                    nrr -= 1
                else:
                    nbr -= 1
            elif d == 2:
                if nrc > nbc:
                    nrc += 1
                else:
                    nbc += 1
            else:
                if nrc < nbc:
                    nrc -= 1
                else:
                    nbc -= 1


        return solution((nrr, nrc), (nbr, nbc), cnt+1)


solution(red, blue, 0)
print(result)