import sys
sys.stdin = open('input.txt')

def Calculator(N, s):
    stack = []
    new_s = ''
    calculat = []
    # 1. 중위표현식 > 후위표현식
    for i in range(N):
        if 48 <= ord(s[i]) <= 57: # 숫자이면
            new_s += s[i]
        else: # 숫자가 아니고
            if not stack: # 스택이 비어있으면
                stack.append(s[i]) # 스택에 넣자
            else: #스택이 비어있지 않으면, + 들어있는 상태
                new_s += stack.pop() # 스택에 있던 +를 빼서 new_s에 붙이고
                stack.append(s[i]) # 이번에 나온 +를 스택에 넣어라

    # 중위 표현식은 숫자로 끝난다. 그렇다는 것은 스택에 무조건 +가 남아있다.
    # 그래서 마지막에 스택에 있던 +를 new_s에 붙여 마무리한다.
    new_s += stack.pop()
    #print(new_s)

    # 2. 후위표현식 > 계산
    for i in range(len(new_s)):
        if 48 <= ord(new_s[i]) <= 57: # 숫자이면
            calculat.append(int(new_s[i]))
        else: # + 가 나오면
            calculat[0] += int(calculat.pop()) # top을 빼서 calculat[0]에 더한다

    return calculat[0]


for tc in range(1, 11):
    N = int(input())
    s = input()
    print('#{} {}'.format(tc, Calculator(N, s)))


