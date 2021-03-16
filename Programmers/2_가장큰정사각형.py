def solution(board):
    result = []
    max_square = min(len(board), len(board[0]))
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]:
                next = 1
                while i + next < len(board) and j + next < len(board[i]):
                    temp_cnt = 0
                    for k in range(next + 1):
                        for l in range(next + 1):
                            if board[i + k][j + l] == 1:
                                temp_cnt += 1
                    if temp_cnt == (next + 1) ** 2:
                        next += 1
                    else:
                        break
                if next == max_square:
                    return max_square**2
                else:
                    result.append(next)
    print(result)
    if result:
        return max(result) ** 2
    else:
        return 0


print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))