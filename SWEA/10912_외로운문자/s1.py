import sys
sys.stdin = open('eval_input.txt')

for tc in range(1, int(input())+1):
    s = list(input())
    stack = []
    for i in range(len(s)):
        # 스택이 비었으면 넣고
        if not stack:
            stack.append(s[i])
        # 스택에 중복된게 없으면 넣고
        elif s[i] not in stack:
            stack.append(s[i])
        # 스택에 있으면, 스택에 있는거 빼고
        elif s[i] in stack:
            stack.remove(s[i])

    if not stack:
        print('#{} Good'.format(tc))
    else:
        print('#{} {}'.format(tc, ''.join(sorted(stack))))
