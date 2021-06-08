import sys
sys.stdin = open('eval_input.txt')

def SelectBlue(color):
    # 최소 변경 횟수
    min_change = 99999999999999999

    # 파란색 시작 인덱스
    for idx in range(len(color)):
        # 파란색 몇줄 만들건지?
        for howmany in range(1, len(color) - idx + 1):
            # 변경 횟수
            cnt = 0
            # 전체 길이를 순회하면서
            for i in range(len(color)):
                # idx 이전 = 흰색
                if i < idx: cnt += M - color[i][0]
                # idx ~ idx+ howmany = 파란색
                elif i < idx + howmany: cnt += M - color[i][1]
                # 그 이후 = 빨간색
                else: cnt += M - color[i][2]
                if cnt >= min_change : break

            # 최소값 갱신
            if cnt < min_change:
                min_change = cnt

    return min_change


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    flag = [ list(input()) for _ in range(N)]

    result = 0
    color = []

    # 각 행마다 무슨색이 몇개있는지 부터 확인해보자
    for i in range(N):
        # W, B, R
        temp = [0, 0, 0]
        for j in range(M):
            if flag[i][j] == 'W': temp[0] += 1
            elif flag[i][j] == 'B': temp[1] += 1
            else: temp[2] += 1
        color.append(temp)

    # 맨앞 맨뒤는 무조건 W, R니까 다른색이었던 개수들 더하기
    result += (M - color[0][0]) + (M - color[-1][2])

    # 맨앞 맨뒤 제거(이제 볼 필요X)
    color.pop(0)
    color.pop()

    # N이 3이었으면 중간 무조건 파란색이라, 함수들어가지 말고 바로 결과
    if len(color) == 1:
        result += M - color[0][1]
        print('#{} {}'.format(tc, result))

    # 남아있는 color 중에 파란색은 적어도 한줄, 나머지는 있어도 되고 없어도 됨
    # 파란색의 경우의 수 : 몇번 인덱스에서 시작할 것인가 / 몇줄 만들 것인가
    # 인덱스 후보 : 0 ~ len(color)-1 몇줄 후보 : len(color) ~ 1
    else:
        result += SelectBlue(color)
        print('#{} {}'.format(tc, result))



