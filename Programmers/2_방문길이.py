def solution(dirs):
    # 좌표평면은 11*11(0~10) 시작위치 [5,5]
    # 방문한 정점의 갯수만 세면 됨

    # 보드 만들기
    r, c = 5, 5

    # 이동
    order = {'U': [-1, 0], 'D': [1, 0], 'L': [0, -1], 'R': [0, 1]}

    # 이동 경로
    path = []

    for dir in dirs:
        # 입력값대로 이동할 좌표 확인
        nr = r + order[dir][0]
        nc = c + order[dir][1]

        # 인덱스 안넘었다면(이동가능하면)
        if 0 <= nr <= 10 and 0 <= nc <= 10:
            # 이동 경로 저장(출발 > 도착)
            path.append([r, c, nr, nc])
            # 실제로 이동
            r, c = nr, nc

    overlap = 0

    # 맨앞 경로는 겹칠 수 없으니 1번부터 확인
    for i in range(1, len(path)):
        # 내 앞 경로랑 확인
        for j in range(i):
            # 만약 겹치는 경로가 있으면,
            if path[i] == path[j]:
                # 중복 경로 +1
                overlap += 1
                break
            # 같은 길을 > 이렇게 간거랑 < 간거랑 시점 종점은 반대이지만
            # 중복 경로로 처리해야 한다.
            elif path[i][:2] == path[j][2:] and path[j][:2] == path[i][2:]:
                # 중복 경로 +1
                overlap += 1
                break

    # 전체 이동 거리 - 중복 경로 개수
    return len(path) - overlap


print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))
print(solution("UDUDUDUDUDUDUD"))