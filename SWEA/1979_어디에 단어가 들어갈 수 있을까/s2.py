import sys
sys.stdin = open('input.txt', 'r', encoding = 'UTF-8')

def Where(N, M, puzzle):
    # 단어가 들어갈 수 있는 자리 갯수
    cnt = []
    for i in range(N):
        temp_cnt = 0
        for j in range(N):
            # 1이 나오면 등장횟수를 +1
            if puzzle[i][j] == 1:
                temp_cnt += 1
            # 0이 나오면 지금까지 더해졌던 temp_cnt를 cnt에 추가하고
            # temp_cnt 초기화(연속이 깨진경우)
            else:
                cnt.append(temp_cnt)
                temp_cnt = 0
        # 행이 끝나면 쌓여있던 temp_cnt를 cnt에 추가
        cnt.append(temp_cnt)

    for i in range(N):
        temp_cnt = 0
        for j in range(N):
            if puzzle[j][i] == 1:
                temp_cnt += 1
            else:
                cnt.append(temp_cnt)
                temp_cnt = 0
        cnt.append(temp_cnt)
    print(cnt)

    result = 0
    for space in cnt:
        if space == M:
            result += 1

    return result


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    puzzle = []
    for _ in range(N):
        puzzle.append(list(map(int, input().split())))
    print('#{} {}'.format(tc, Where(N, M, puzzle)))