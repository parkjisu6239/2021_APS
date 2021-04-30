def solution(rows, columns, queries):
    arr = [] # 행렬 만들기
    for i in range(rows):
        temp = []
        for j in range(columns * i + 1, columns * (i + 1) + 1):
            temp.append(j)
        arr.append(temp)

    answer = [] # 결과

    # otherclockwise
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]

    for rs, cs, re, ce in queries:
        rs, cs, re, ce = rs - 1, cs - 1, re - 1, ce - 1  # 인덱스
        min_val = 987654321 # 회전값중 최소값
        here = arr[rs][cs] # 가장 마지막에 입력할 시작점 값
        r, c = rs, cs
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k] # 이동
            while rs <= nr <= re and cs <= nc <= ce:
                min_val = min(min_val, arr[nr][nc]) # 최소값 갱신
                arr[r][c] = arr[nr][nc] # 다음값으로 갱신
                r, c = nr, nc
                nr, nc = r + dr[k], c + dc[k]
            if k == 3:
                arr[r][c+1] = here
                min_val = min(min_val, here)
        answer.append(min_val)

    return answer

print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))