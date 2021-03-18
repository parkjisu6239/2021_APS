def solution(maps):
    # 도착지
    end = [len(maps), len(maps[0])]

    # 맵에 테두리 둘러주기
    safe_map = [[0] * (len(maps[0]) + 2)]
    for map in maps:
        safe_map.append([0] + map + [0])
    safe_map.append([0] * (len(maps[0]) + 2))

    # BFS
    # que, 지나온 길은 1이 아닌 다른 숫자로 처리
    que = [[1, 1]]
    safe_map[1][1] = 0

    # 4방향 이동
    dr = [1, -1, 0, 0]
    dc = [0, 0, -1, 1]

    # 거리계산과, 길을 혼동하지 않도록 음수로 처리
    distance = -1

    # Que에 값이 있으면
    while que:
        # 도착지에 방문한 경우, 거리 리턴
        if safe_map[end[0]][end[1]] != 1:
            return -safe_map[end[0]][end[1]] + 1

        # 큐 원소 팝
        r, c = que.pop(0)

        # 4방향 확인, 갈 수 있는 곳 큐에 담기
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            # 길이면
            if safe_map[nr][nc] == 1:
                # 추가, 방문표시는 시점과의 거리로
                que.append((nr, nc))
                safe_map[nr][nc] = distance

        # 동일 거리의 노드가 큐에서 모두 빠지면, 거리 +1
        if que and safe_map[r][c] != safe_map[que[0][0]][que[0][1]]:
            distance -= 1

    return -1

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))