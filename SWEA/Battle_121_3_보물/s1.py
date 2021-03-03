import sys
sys.stdin = open('input.txt')


def TreasurHunter(K, N, key, treasure):
    opend = [0] * N
    order = []
    while key:
        flag = 0
        for i in range(N):
            if treasure[i][0] in key and opend[i] == 0:
                flag += 1
                opend[i] = 1 # 열고
                if i+1 not in order:
                    order.append(i+1) # 상자를 열면 상자번호를 순서에 담자
                key.remove(treasure[i][0]) # 키가 손상되었으니 버리고
                for j in range(treasure[i][1]):
                    if treasure[i][2+j] not in key:
                        key.append(treasure[i][2+j]) # 오픈한 상자에 있는 열쇠 줍줍

        if sum(opend) == N:
            return ' '.join(map(str, order))

        if flag == 0:
            return 'IMPOSSIBLE'


    if sum(opend) == N:
        return order
    else:
        return 'IMPOSSIBLE'


for tc in range(1, int(input())+1):
    K, N = map(int, input().split())
    key = list(map(int, input().split()))
    treasure = [ list(map(int, input().split())) for _ in range(N)]

    print('#{} {}'.format(tc, TreasurHunter(K, N, key, treasure)))