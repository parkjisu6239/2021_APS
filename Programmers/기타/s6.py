def solution(a, b):
    memo = {0: 1, 1: a}

    def recur(a, b):
        if memo.get(b, 0):
            pass
        elif b % 2 == 0:
            memo[b] = recur(a, b//2)**2
        elif b % 2 == 1:
            memo[b] = a * recur(a, b // 2) ** 2

        if memo[b] > 99999:
            memo[b] %= 100000
        return memo[b]

    return recur(a, b)

print(solution(2, 26))