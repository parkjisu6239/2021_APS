def solution(n, k):

    people = list(range(1, n + 1))
    sel = [0] * n
    visit = [0] * n
    cnt = 0
    answer = []


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

    perm(0)

    return answer

print(solution(3, 5))