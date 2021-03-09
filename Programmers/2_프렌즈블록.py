def solution(m, n, board):
    # 2*2가 같은지 보는건 SWEA에서 파리채랑 같다.
    # 2*2가 겹쳐있는 (예제 이미지에서 라이언) 경우가 문제다
    # 현재 상태에서 2*2가 같은 블록의 좌표를 스택에 담는다.
    # 위에서 아래로 사라지는 형태라서 행렬을 반대, 위아래 반대로 저장하는게 나을 것 같다.
    # 스택을 셋으로 바꾸고, 다시 리스트로 바꿔서 길이를 세고
    # 블록을 사라지게 한다(뒤에서부터 팝)

    blockes = [list(pan[::-1]) for pan in zip(*board)]

    # 현재인덱스, 오른쪽, 아래, 대각선 확인
    dr = [0, 0, 1, 1]
    dc = [0, 1, 0, 1]

    # 삭제한 블록 수
    result = 0
    while True:
        # 삭제할 블록의 좌표를 담을 스택
        stack = []
        # 파리채 문제 인덱스 관리와 같음
        for i in range(len(blockes) - 1):
            for j in range(len(blockes[i]) - 1):
                # 현재 인덱스 근처를 확인할 임시 리스트
                temp = []
                for k in range(4):
                    nr = i + dr[k]
                    nc = j + dc[k]
                    # 인덱스를 넘지 않고, 현재 인덱스랑 같으면, 추가
                    if nc < len(blockes[nr]) and blockes[i][j] == blockes[nr][nc]:
                        temp.append([nr, nc])
                    # 다른게 하나라도 나오면 즉시 temp 초기화하고 종료
                    else:
                        temp = []
                        break

                # 위에서 구한 좌표중에서 stack에 없는거만 담는다
                for tem in temp:
                    if tem not in stack:
                        stack.append(tem)

        # 전체 인덱스 다 돌았는데, 스택이 비었으면(삭제할 수 있는게 없으면) 종료
        if not stack:
            break

        # 삭제한 개수 추가
        result += len(stack)
        # 뒤에서부터 삭제할거라서, 오류를 없애기 위해 sort
        stack.sort()
        # 뒤(위)에서 부터 삭제
        for i in range(len(stack) - 1, -1, -1):
            blockes[stack[i][0]].pop(stack[i][1])

    return result

print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))