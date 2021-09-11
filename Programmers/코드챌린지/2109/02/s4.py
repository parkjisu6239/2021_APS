def solution(grid):
    R = len(grid)
    C = len(grid[0])
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    dir = {'S': 0, 'L': -1, 'R': 1}
    P = []
    answer = []

    for r in range(R):
        for c in range(C):
            # r, c는 출발점 / k는 출발 방향
            for k in range(4):
                p = {} # 부모정보(크루스컬)
                flag = False # 종료조건
                while True:
                    # 이동
                    nr, nc = r + dr[k], c + dc[k]

                    # 넘어간 경우 반대방향으로
                    nr %= R
                    nc %= C

                    # 방향 전환
                    k_ = (k + dir[grid[nr][nc]]) % 4

                    # 순환하는 사이클인지 확인
                    if p.get((r, c, k), 0) and p[(r, c, k)] == (nr, nc, k_):
                        P.append(p)
                        break

                    # 기존 경로와 동일한지 확인
                    for parent in P:
                        if parent.get((r, c, k), 0) and parent[(r, c, k)] == (nr, nc, k_):
                            flag = True
                            break

                    if flag:
                        break

                    # 기록 및 갱신
                    p[(r, c, k)] = (nr, nc, k_)
                    r, c = nr, nc
                    k = k_

    for p in P:
        answer.append(len(p))
    return sorted(answer)



print(solution(["SL","LR"]))
print(solution(["S"]))
print(solution(["R","R"]))