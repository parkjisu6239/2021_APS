def solution(sticker):
    N = len(sticker)

    if N < 3:
        return max(sticker)

    # DP[i] = i번까지 선택할 수 있는 최대합
    DP = [0] * N

    # 0번스티커 선택, 1번 미선택으로 시작
    # 즉, 1번까지 총합 sticker[0]이며, 0번을 선택했기때문에 맨마지막은 선택 불가!
    DP[0], DP[1] = sticker[0], sticker[0]
    for i in range(2, N-1):
        DP[i] = max(DP[i-1], DP[i-2]+sticker[i])
    max_total = max(DP)

    # 0번스티커 미선택, 0번 선택으로 시작
    # 0번까지는 총합 0, 1번까지는 sticker[1], 마지막것도 선택 가능
    DP[0], DP[1] = 0, sticker[1]
    for i in range(2, N):
        DP[i] = max(DP[i - 1], DP[i - 2] + sticker[i])
    max_total = max(max_total, max(DP))

    return max_total


print(solution([14, 6, 5, 11, 3, 9, 2, 10]))