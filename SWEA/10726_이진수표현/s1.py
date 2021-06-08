import sys
sys.stdin = open("eval_input.txt")

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())

    # 30 = 16 + 8 + 4 + 2 > 1(1110) 뒤에 4개?

    result = 'OFF'
    for i in range(N):
        if not M & (1 << i):
            break
    else:
        result = 'ON'

    print('#{} {}'.format(tc, result))