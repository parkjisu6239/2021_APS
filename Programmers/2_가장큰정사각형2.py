def solution(board):
    N = min(len(board), len(board[0]))
    for n in range(N, 0, -1):
        for i in range(len(board) - n + 1):
            for j in range(len(board[0]) - n + 1):
                square = 0
                for k in range(n):
                    square += sum(board[i+k][j: j + n])
                if square == n ** 2:
                    return square
    return 0

print(solution([[0, 0, 1, 1], [1, 1, 1, 1]]))