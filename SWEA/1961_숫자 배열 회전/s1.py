import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    N = int(input())
    numbers = [ list(map(int, input().split())) for _ in range(N)]

    # 90도 회전은 열은 고정하고, 행을 아래에서 위로 읽는 형태랑 같음
    rotate_90 = []
    for j in range(N):
        temp = []
        for i in range(N-1, -1, -1):
            temp.append(numbers[i][j])
        rotate_90.append(temp)

    # 90도 돌린걸 또 돌리기
    rotate_180 = []
    for j in range(N):
        temp = []
        for i in range(N-1, -1, -1):
            temp.append(rotate_90[i][j])
        rotate_180.append(temp)

    # 또 돌리기
    rotate_270 = []
    for j in range(N):
        temp = []
        for i in range(N - 1, -1, -1):
            temp.append(rotate_180[i][j])
        rotate_270.append(temp)

    # 출력
    print('#{}'.format(tc))
    for i in range(N):
        print(''.join(map(str, rotate_90[i])), ''.join(map(str, rotate_180[i])), ''.join(map(str, rotate_270[i])))

