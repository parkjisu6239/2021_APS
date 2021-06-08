import sys
sys.stdin = open('eval_input.txt')

def Cal(arr):
    stack = []
    for i in range(len(arr)):
        if arr[i].isdigit():
            stack.append(int(arr[i]))
        else:
            # 처음에는 이 if문과 elif 순서를 반대로 했더니 9맞고 1개 틀림
            # if-elif는 조건문 1개에 부합하면, 그 아래것은 실행이 안되어서
            # elif로 안들어가기 때문! 그래서 아래처럼 '.'부터 검사하거나,
            # 순서 상관없이 하려면 if-if로!
            if arr[i] == '.':
                if len(stack) == 1:
                    return stack.pop()
                else:
                    return 'error'
            elif len(stack) >= 2:
                b = stack.pop()
                a = stack.pop()
                if arr[i] == '+':
                    stack.append(a + b)
                elif arr[i] == '*':
                    stack.append(a * b)
                elif arr[i] == '-':
                    stack.append(a - b)
                elif arr[i] == '/':
                    stack.append(a // b)
            else:
                return 'error'


for tc in range(1, int(input())+1):
    arr = list(map(str, input().split()))
    print('#{} {}'.format(tc, Cal(arr)))
