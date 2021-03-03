import sys
sys.stdin = open("input.txt")

def Sadarytagi(sadary):

    # 사다리를 밑에서 위로 오르는 것이라서 이동방향은 좌,우,위 중에 하나
    # 시작점 찾기(sadary의 마지막행의 요소중 2인 값의 인덱스로 시작) .index(2) 쓰면 편-안
    # y = sadary[99].index(2)
    for i in range(100):
       if sadary[99][i] == 2:
            y = i
            break

    # 바닥부터 시작
    x = 99
    # 이동방향은 좌,우,상
    go_x = [0, 0, -1]
    go_y = [-1, 1, 0]
    # 0으로 초기화
    k = 0

    # 맨위에 도달하기 전까지 반복
    while x:
        # 이동방향이 왼쪽일때
        if k == 0:
            # 왼쪽으로 더 갈수 있으면 왼쪽으로 가
            if y > 0 and sadary[x + go_x[k]][y + go_y[k]]:
                x += go_x[k]
                y += go_y[k]
            # 왼쪽으로 못가면 위로 가
            else:
                k = 2
                x += go_x[k]
                y += go_y[k]
        # 이동방향이 오른쪽일 때
        elif k == 1:
            # 오른쪽으로 더 갈수 있으면 오른쪽으로 가
            if y < 99 and sadary[x + go_x[k]][y + go_y[k]]:
                x += go_x[k]
                y += go_y[k]
            # 오른쪽으로 못가면 위로 가
            else:
                k = 2
                x += go_x[k]
                y += go_y[k]
        # 이동방향이 위쪽일 때
        else:
            # 왼쪽에 길이 있으면 왼쪽을 봐(가지는 말고)
            if y > 0 and sadary[x + go_x[0]][y + go_y[0]]:
                k = 0
            # 오른쪽에 길이 있으면 오른쪽을 봐(가지는 말고)
            elif y < 99 and sadary[x + go_x[1]][y + go_y[1]]:
                k = 1
            # 양쪽에 둘다 길이 없으면 그냥 앞으로 가
            else:
                x += go_x[k]
                y += go_y[k]

        if x == 0:
            return y

for _ in range(10):
    tc = int(input())
    sadary = []
    for _ in range(100):
        sadary.append(list(map(int, input().split())))
    print('#{} {}'.format(tc, Sadarytagi(sadary)))