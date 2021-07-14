def solution(board, moves):
    stack = []
    answer = 0
    for move in moves :
        for i in range(len(board)):
            if board[i][move - 1] != 0:
                stack.append([board[i][move - 1]])
                board[i][move - 1] = 0
                break
        if len(stack) > 1:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
                answer += 2
    print(stack)
    return answer