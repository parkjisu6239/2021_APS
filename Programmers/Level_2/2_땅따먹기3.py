def solution(land):
    #print(land)

    # 땅을 계속 현재행+이전행 선택결과의 최대값으로 갱신
    # 현재 행에서는 이전에 밟은거랑 같은 열이 아니고, 최대가 되게끔
    # 그리디 너낌..? 현재행에서 할수 있는 최대값만 찾는 방법

    N = len(land)
    for i in range(1, N):
        land[i][0] = land[i][0] + max(land[i - 1][1], land[i - 1][2], land[i - 1][3])
        land[i][1] = land[i][1] + max(land[i - 1][0], land[i - 1][2], land[i - 1][3])
        land[i][2] = land[i][2] + max(land[i - 1][0], land[i - 1][1], land[i - 1][3])
        land[i][3] = land[i][3] + max(land[i - 1][0], land[i - 1][1], land[i - 1][2])

    #print(land)

    return max(land[N-1])


print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))