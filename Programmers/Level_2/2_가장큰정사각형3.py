def solution(board):
    N = min(len(board), len(board[0]))
    for n in range(N, 0, -1):
        for i in range(len(board) - n + 1):
            j = 0
            while j < len(board[0]) - n + 1:
                square = 0
                index_0 = 0
                for k in range(n):
                    for l in range(n):
                        if board[i + k][j + l] == 0:
                            if j + l > index_0:
                                index_0 = j + l
                        square += board[i + k][j + l]
                if square == n ** 2:
                    return square
                j += index_0 + 1

    return 0

print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
print(solution([[0, 0, 1, 1], [1, 1, 1, 1]]))