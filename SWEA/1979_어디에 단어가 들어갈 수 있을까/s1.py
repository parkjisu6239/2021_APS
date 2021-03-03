import sys
sys.stdin = open('input.txt', 'r', encoding = 'UTF-8')

def Where(N, M, puzzle):
    # 단어가 들어갈 수 있는 자리 갯수
    cnt = 0
    # 가로 기준으로 탐색
    for i in range(N):
        j = 0
        # 구간합 범위
        while j < N-M+1:
            for k in range(M):
                # 1인곳을 찾아야되서 0이면 다음 열을 탐색하게 하고 break
                if puzzle[i][j+k] == 0:
                    j += 1
                    break
            # break 없이 M만큼 1로 채워진 경우
            else:
                # 1이 연속되고, 그 연속된 1이 퍼즐모양의 끝인 경우 :  ~111(끝)
                # 혹은 1의 연속 뒤에 0이 나올 경우 : ~1110~
                # 이 경우가 딱 단어의 길이에 맞는 1의 연속이 있는 경우!
                if j + M >= N or puzzle[i][j + M] == 0 :
                    # 갯수를 올리고, 현재 패턴(1의 연속)이 끝나는 지점부터
                    # 다시 찾게 함
                    cnt += 1
                    j += M
                # 1의 M만큼 연속 뒤에 또 1이 나온 경우
                # 1이 딱 M만큼만 연속되야 거기에 들어갈 수 있다고 했으므로, 카운트 올리지 않고
                # 연속된 패턴을 뛰어넘어감
                elif puzzle[i][j + M] == 1:
                    j += M + 1

    for i in range(N):
        j = 0
        while j < N - M + 1:
            for k in range(M):
                if puzzle[j+k][i] == 0:
                    j += 1
                    break
            else:
                if j + M == N or puzzle[j + M][i] == 0 :
                    cnt += 1
                    j += M
                elif puzzle[j + M][i] == 1:
                    j += M + 1

    return cnt


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    puzzle = []
    for _ in range(N):
        puzzle.append(list(map(int, input().split())))
    print('#{} {}'.format(tc, Where(N, M, puzzle)))