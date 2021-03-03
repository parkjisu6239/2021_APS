import sys
sys.stdin = open('input.txt')

def PaperCount(N):
    # 1 > 1
    # 2 > 3
    # 3 > 5
    # 4 > 11
    # 5 > 21
    # 6 > 43
    # 7 > 85
    # 전전*2 + 전

    stack = [0, 1, 3]
    if N//10 == 1:
        return stack[1]
    elif N//10 == 2:
        return stack[2]
    else:
        for _ in range(3, N//10 + 1):
            stack.append(stack[-2]*2 + stack[-1])
        return stack[N//10]


for tc in range(1, int(input())+1):
    N = int(input())
    print('#{} {}'.format(tc, PaperCount(N)))