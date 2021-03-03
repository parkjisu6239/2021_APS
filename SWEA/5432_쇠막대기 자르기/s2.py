import sys
sys.stdin = open('input.txt', 'r', encoding = 'UTF-8')

def Cut_pipe(pipe):
    stack = []
    cut_cnt = 0
    for i in range(len(pipe)):
        # 여는 괄호가 나오면 스택에 쌓자
        if pipe[i] == '(':
            stack += '('
        # 닫는 괄호가 연속으로 나오면, 이번에 나온 닫는 괄호는
        # 레이저가 아니라 막대의 끝이기때문에 스택에서 막대기 하나 빼고
        # 잘린 갯수에 +1
        elif pipe[i] == ')' and pipe[i-1] == ')':
            stack.pop()
            cut_cnt += 1
        # 여는괄호 다음에 닫는 괄호 나온 경우 (레이저)
        # 지금까지 쌓인 막대기 개수만큼 조각수를 더하라
        else:
            stack.pop()
            cut_cnt += len(stack)

    return cut_cnt



for tc in range(1, int(input())+1):
    pipe = input()
    print('#{} {}'.format(tc, Cut_pipe(pipe)))