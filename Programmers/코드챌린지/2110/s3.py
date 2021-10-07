def solution(n, m, x, y, queries):
    query = {0: (0, -1), 1: (0, 1), 2: (-1, 0), 3: (1, 0)}
    dp = {i: [] for i in range(1, len(queries)+1)}
    answer = 0

    def go(r, c, queries):
        path = []
        for idx, (d, w) in enumerate(queries):
            dr, dc = query[d]
            r += dr
            c += dc
            if r < 0: r = 0
            if r >= n: r = n - 1
            if c < 0: c = 0
            if c >= m: c = m - 1

            if (r, c) in dp[idx+1]:
                return 1
            path.append((r, c))

        if (r, c) == (x, y):
            for i, pos in enumerate(path):
                dp[i+1].append(pos)
            return 1

        return 0

    for r in range(n):
        for c in range(m):
            answer += go(r, c, queries)
    return answer


print(solution(2, 5, 0, 1, [[3,1],[2,2],[1,1],[2,3],[0,1],[2,1]]))
