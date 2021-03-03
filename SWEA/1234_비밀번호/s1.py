import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N, numbers = map(str, input().split())

    # 스택
    stack = []
    # 인풋의 길이만큼 반복
    for i in range(int(N)):
        # 비어 있으면 그냥 넣자
        if not stack:
            stack.append(numbers[i])
        # 새로 넣으려는 값이 스택의 탑에 있으면 연속문자니까 뽑자
        elif stack[-1] == numbers[i]:
            stack.pop()
        # 그게 아니면 넣자
        else:
            stack.append(numbers[i])

    print('#{} {}'.format(tc, ''.join(stack)))