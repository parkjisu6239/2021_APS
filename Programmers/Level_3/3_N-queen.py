def solution(n):
    answer = 0
    
    # sel : (행, 열) = (i, sel[i]) 위치에 퀸을 놓았다는 의미
    sel = [0] * n
    # visit : 인덱스 = 열 에 퀸이 놓아져있는지, 아닌지 (1, 0)
    visit = [0] * n

    # 대각선상 위치인지 확인
    def isdiagonal(x1, y1, x2, y2):
        if abs(x2 - x1) == abs(y2 - y1):
            return True
        else:
            return False

    # 백트래킹
    def queen(idx):
        nonlocal answer
        # 모두 만족해서, n개를 놨으면 결과 +1
        if idx == n:
            answer += 1
            return

        # idx 행에 어느 열에 퀸을 놓을지 확인
        for i in range(n):
            # 위에서 퀸을 놓은 적 없는 열 중에
            if visit[i] == 0:
                # 첫번째 행은 아무데나 놔도 됨
                if idx == 0:
                    visit[i] = 1
                    sel[idx] = i
                    queen(idx + 1)
                    visit[i] = 0
                # 두번째 행부터
                else:
                    # 앞서 놓아진 퀸의 위치 확인
                    for j in range(len(sel[:idx])):
                        # 대각선상에 겹치는게 하나라도 있으면 break
                        if isdiagonal(j, sel[j], idx, i):
                            break
                    # 없으면, 그 열에 퀸을 놓자
                    else:
                        visit[i] = 1
                        sel[idx] = i
                        queen(idx + 1)
                        # 더 이상 놓수 없어서 돌아온 경우, 놓았던 퀸 빼자
                        visit[i] = 0

    queen(0)

    return answer


print(solution(4))