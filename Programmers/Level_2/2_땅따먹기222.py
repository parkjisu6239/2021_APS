def solution(land):
    N = len(land)

    sel = [0] * 4

    max_sum = 0
    total = 0

    def Eat_land(idx):
        global total, max_sum

        if idx == N:
            if total > max_sum:
                max_sum = total
            return

        for i in range(4):
            if idx != 0:
                if sel[idx - 1] == i:
                    continue
                else:
                    sel[idx] = i
                    total += land[idx][i]
                    Eat_land(idx + 1)
                    sel[idx] = 0
                    total -= land[idx][i]
            else:
                sel[idx] = i
                total += land[idx][i]
                Eat_land(idx + 1)
                sel[idx] = 0
                total -= land[idx][i]

    Eat_land(0)

    return max_sum


print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))