import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    Q = list(map(int, input().split()))

    for _ in range(M):
        Q.append(Q.pop(0))

    print('#{} {}'.format(tc, Q[0]))