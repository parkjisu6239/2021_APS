def solution(board):
    # 행,렬 1~끝을 순회하고 인덱스 기준 현위치,좌상,좌,상 4군데를 확인한다
    # 현위치의 값을 4개의 값중 최솟값 + 1로 바꾼다.

    # 가로세로중 길이가 1인게 있으면 위 방식으로 탐색 불가하고, 정사각형 길이는 무조건 1밖에 안됨
    if len(board) == 1 or len(board[0]) == 1:
        return 1

    # 최대길이를 구하자
    max_len = 0
    for r in range(1, len(board)):
        for c in range(1, len(board[0])):
            # 현위치 기준 2X2탐색, 현위치가 1인 경우만 갱신
            if board[r][c]:
                # 4개 값중 최소값 + 1
                # 중간에 0이 있더라도 1이니까 값에는 변화 없음
                board[r][c] = min(board[r-1][c], board[r-1][c-1], board[r][c-1]) + 1
                # 갱신된 길이가 최대면 그 값을 최대길이로
                if board[r][c] > max_len:
                    max_len = board[r][c]
    return max_len**2

print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
print(solution([[0, 0, 1, 1], [1, 1, 1, 1]]))

# [0, 1, 1, 1]
# [1, 1, 2, 2]
# [1, 2, 2, 3]
# [0, 1, 2, 3]