def solution(number, k):
    N = len(number)
    visit = [0] * N
    result = []

    def DFS(idx, N, k, visit, result):
        if idx == k:
            total = ''
            for i in range(N):
                if not visit[i]:
                    total += number[i]
            result.append(int(total))
            return

        for i in range(N):
            if not visit[i]:
                visit[i] = 1
                DFS(idx+1, N, k, visit, result)
                visit[i] = 0

    DFS(0, N, k, visit, result)

    return str(max(result))


print(solution("4177252841", 4))