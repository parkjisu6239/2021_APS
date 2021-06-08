import sys
sys.stdin = open('eval_input.txt')

for tc in range(1, int(input())+1):
    D, A, B, F = map(int, input().split())

    # 속력! 시간이 필요
    # 기차사이의 거리 = D - (A + B)*t
    # 그 안에서 파리가 왔다갔다 한다.

    # 기차가 충돌한 시간
    time = D / (A + B)

    # 그 시간동안 파리가 살아있고, 그동안 계속 왔다갔다 F 속력으로 움직였을테니까
    # 거리 = 속력 * 시간
    print('#{} {}'.format(tc, time*F))
