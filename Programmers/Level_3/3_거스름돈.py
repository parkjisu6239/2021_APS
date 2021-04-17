def solution(n, money):
    # 재귀!
    sel = [0] * len(money)
    result = 0
    visit = {}

    def change(sel, don):
        nonlocal result
        if visit.get((don, *sel), 0):
            return

        if don == n:
            visit[(don, *sel)] = 1
            result = (result + 1)%1000000007

            return

        if don > n:
            return

        visit[(don, *sel)] = 1

        for i in range(len(money)):
            if don + money[i] <= n:
                sel[i] += 1
                change(sel, don + money[i])
                sel[i] -= 1

    change(sel, 0)

    return result%1000000007


print(solution(5, [1, 2, 5]))