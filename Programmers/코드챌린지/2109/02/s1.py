def solution(grid):
    R = len(grid)
    C = len(grid[0])
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    dir = {'S': 0, 'L': -1, 'R': 1}

    path = []
    for r in range(R):
        for c in range(C):
            # r, c는 출발점
            for k in range(4): # 출발 방향
                temp = [(r, c, k)]
                flag = False
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
                            flag = True
                            break

                    if flag:
                        path.append(temp[:-1])
                        break

                    temp.append((nr, nc, k_))  # 경로 기록
                    r, c = nr, nc # 변경
                    k = k_

    isBreak = False
    for p in range(len(path)-1, 0, -1):
        for t in range(p):
            if isBreak:
                isBreak = False
                break
            for pi in range(len(path[p])):
                if path[t][0] == path[p][pi] and path[t][1] == path[p][(pi+1)%len(path[p])]:
                        path.pop()
                        isBreak = True
                        break

    answer = []
    for p in path:
        answer.append(len(p))

    return answer


print(solution(["SL","LR"]))
print(solution(["S"]))
print(solution(["R","R"]))