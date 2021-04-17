def solution(n, results):
    # 정점 v의 조상수 + 자손수 = n-1이면 순위 확정 가능

    # idx가 이긴경우 상대방들, idx가 진경우 상대방들
    node = [[[], []] for _ in range(n + 1)]
    for win, lose in results:
        node[win][0].append(lose)
        node[lose][1].append(win)

    # 이긴or진사람들, 이긴or진경우
    def play(win_lose, r):
        if not win_lose: # 빈리스트면 0
            return 0

        # 사람들을 que에 담는다
        que = list(win_lose)
        visit = [0] * (n + 1)

        while que:
            s = que.pop(0)
            visit[s] = 1

            for e in node[s][r]:
                if visit[e] == 0:
                    visit[e] = 1
                    que.append(e)

        # 방문한 노드의 수(모든 자손수 or 조상수)
        return sum(visit)

    result = 0

    for v in range(1, n + 1):
        # 조상수(나보다 못하는 사람들) + 자손수(나보다 잘하는 사람들) = n-1이면 순위 확정
        if play(node[v][0], 0) + play(node[v][1], 1) == n-1:
            result += 1

    return result


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))