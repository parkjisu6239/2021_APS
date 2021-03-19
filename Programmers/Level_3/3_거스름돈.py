def solution(n, money):
    # SWEA 수영장 문제랑 비슷 근데 시간 초과됨!
    answer = []
    result = 0
    sel = [0] * len(money)

    def change(don):
        nonlocal answer, result
        if don == n:
            if sel not in answer:
                result += 1
                result %= 1000000007
                answer.append(list(sel))
            return

        if don > n:
            return

        for i in range(len(money)):
            sel[i] += 1
            change(don + money[i])
            sel[i] -= 1

    change(0)

    return result % 1000000007


print(solution(5, [1, 2, 5]))