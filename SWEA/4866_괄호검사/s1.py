import sys
sys.stdin = open('input.txt')

def IsCorrect(T):
    stack = []
    for i in range(len(T)):
        if T[i] == '(' or T[i] == '{':
            stack.append(T[i])
        # 닫는 괄호가 나왔을때
        elif T[i] == ')':
            # 스택이 비어있지 않고, 짝이 맞으면
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return 0
        elif T[i] == '}':
            # 스택이 비어있지 않고, 짝이 맞으면
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                return 0

    if stack:
        return 0
    else:
        return 1


for tc in range(1, int(input())+1):
    T = input()
    print('#{} {}'.format(tc, IsCorrect(T)))