import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    s = input()
    stack = []

    for i in range(len(s)):
        if stack: # 스택이 비어있지 않으면
            if stack[-1] == s[i]: #top과 s[i]가 같으면
                stack.pop() # 중복문자 발견! pop으로 제거
            else: # 중복이 아니면
                stack.append(s[i]) # s[i]를 추가
        else: # 스택이 비어 있으면
            stack.append(s[i]) # 일단 쌓기

    print('#{} {}'.format(tc, len(stack)))