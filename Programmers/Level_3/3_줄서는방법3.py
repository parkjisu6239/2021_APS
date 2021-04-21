def factorial(n):
    if n < 2:
        return n
    else:
        return n * factorial(n - 1)


def solution(n, k):
    # k번째를 구하는 거라서, 처음부터 구할 필요가 없음!
    # 첫번째 원소를 고정했을때, 남은 수들로 만들어지는 경우의 수는 (n-1)!
    facto = factorial(n - 1)

    # 맨앞숫자가 fix는 지나감
    fix = k // facto

    # 맨앞숫자는 fix + 1하고 하면 되고, 구해진 숫자 중에서 k - fix * facto 번째 순열을 찾으면 된다.
    answer = []
    people = list(range(1, n + 1))
    sel = [0] * n
    sel[0] = fix + 1
    visit = [0] * n
    visit[fix] = 1
    cnt = fix*facto

    def perm(idx):
        nonlocal cnt, answer

        if answer:
            return

        if idx == n:
            cnt += 1
            if cnt == k:
                answer = list(sel)
            return


        for i in range(n):
            if visit[i] == 0:
                visit[i] = 1
                sel[idx] = people[i]
                perm(idx + 1)
                visit[i] = 0

    perm(1)

    return answer

print(solution(3, 5))