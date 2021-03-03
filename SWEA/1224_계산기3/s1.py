import sys
sys.stdin = open('input.txt')

def Calculator(N, s):
    stack = []
    new_s = ''
    calculat = []
    Priority = {'+': 1, '*': 2, '(':0}

    # 1. 중위표현식 > 후위표현식
    for i in range(N):
        if 48 <= ord(s[i]) <= 57: # 숫자이면
            new_s += s[i]
        else: # 숫자가 아니고
            if not stack or s[i] == '(': # 스택이 비어있거나 여는 괄호이면
                stack.append(s[i]) # 스택에 넣자
            else: #스택이 비어있지 않으면
                if s[i] == ')': # 닫는 괄호가 나오면
                    while stack[-1] != '(': # 여는 괄호가 나올때까지 팝
                        new_s += stack.pop()
                    # 여는 괄호가 나와서 반복문이 종료되면, 여는 괄호도 팝
                    stack.pop()
                elif Priority[s[i]] > Priority[stack[-1]]: # 우선순위가 높으면
                    stack.append(s[i]) # 스택에 쌓자
                else: # 우선 순위가 낮으면
                    # 우선 순위가 높은게 나오거나, 스택이 비기 전까지
                    # 스택에 쌓인 연산자를 new_s에 붙여라
                    while stack and Priority[s[i]] <= Priority[stack[-1]]:
                        new_s += stack.pop()
                    stack.append(s[i]) # 위 반복문을 나온 후 스택에 값을 추가해라

    # 남아 있는거 털어라
    for i in range(len(stack)):
        new_s += stack.pop()

    # 2. 후위표현식 > 계산
    for i in range(len(new_s)):
        if 48 <= ord(new_s[i]) <= 57: # 숫자이면
            calculat.append(int(new_s[i]))
        elif new_s[i] == '+': # + 가 나오면 더하고
            b = calculat.pop()
            calculat[-1] += b #
        else: # * 이 나오면 곱해라
            b = calculat.pop()
            calculat[-1] *= b

    return calculat[0]


for tc in range(1, 11):
    N = int(input())
    s = input()
    print('#{} {}'.format(tc, Calculator(N, s)))


