def solution(grid):
    R = len(grid)
    C = len(grid[0])
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    dir = {'S': 0, 'L': -1, 'R': 1}
    P = []
    answer = []

    path = []
    for r in range(R):
        for c in range(C):
            # r, c는 출발점
            for k in range(4): # 출발 방향
                temp = [(r, c, k)]
                p = {}
                flag1, flag2 = False, False
                while True:
                    nr, nc = r + dr[k], c + dc[k] # 이동

                    # 넘어간 경우 반대방향으로
                    if nr < 0: nr = R - 1
                    if nr >= R: nr = 0
                    if nc < 0: nc = C - 1
                    if nc >= C: nc = 0

                    k_ = (k + dir[grid[nr][nc]]) % 4  # 방향 전환

                    for i in range(len(temp)-1):
                        if temp[i] == (r, c, k) and temp[i+1] == (nr, nc, k_):
                            flag1 = True
                            break

                    if flag1:
                        path.append(temp)
                        P.append(p)
                        break

                    for parent in P:
                        if parent.get((r, c, k), 0) and parent[(r, c, k)] == (nr, nc, k_):
                            flag2 = True
                            break

                    if flag2:
                        break

                    temp.append((nr, nc, k_))  # 경로 기록
                    p[(r, c, k)] = (nr, nc, k_)
                    r, c = nr, nc # 변경
                    k = k_

    for p in path:
        answer.append(len(p)-1)
    return sorted(answer)



print(solution(["SL","LR"]))
print(solution(["S"]))
print(solution(["S","S"]))