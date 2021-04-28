# 재귀
def solution(sticker):
    N = len(sticker)
    visit = [0] * N
    max_total = 0

    def Collection_Stick(total):
        nonlocal max_total, visit

        if sum(visit) == N:
            if total > max_total:
                max_total = total
            return

        for i in range(N):
            if visit[i] == 0:
                pre_visit = list(visit)
                visit[i] = 1
                visit[i - 1] = 1
                if i == N-1:
                    visit[0] = 1
                else:
                    visit[i+1] = 1
                Collection_Stick(total + sticker[i])
                visit = list(pre_visit)

    Collection_Stick(0)

    return max_total

print(solution([14, 6, 5, 11, 3, 9, 2, 10]))