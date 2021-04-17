def solution(m, n, puddles):
    # 1로 초기화
    land = [[1] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if [i+1, j+1] in puddles: # 웅덩이이면 0
                land[i][j] = 0
            elif i == 0 and j == 0: # 집이면 넘기기
                continue
            elif i == 0: # 첫행은 왼쪽값이랑 같음
                land[i][j] = land[i][j-1]
            elif j == 0: # 첫열은 위쪽값이랑 같음
                land[i][j] = land[i-1][j]
            else: # 왼쪽, 위쪽 더하기
                land[i][j] = (land[i - 1][j] + land[i][j - 1]) % 1000000007

    return land[m-1][n-1]

print(solution(4, 3, [[2, 2]]))