import sys
sys.stdin = open('input2.txt')

H, W = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(H)]


def getDP():
    dp[0][0] = 0

    for i in range(1, H):
        dp[i][0] = dp[i - 1][0] + arr[i][0]

    for j in range(1, W):
        dp[0][j] = dp[0][j - 1] + arr[0][j]

    for i in range(1, H):
        for j in range(1, W):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + arr[i][j]

    return dp[-1][-1]


def findPath():
    r, c = H - 1, W - 1
    path = [(r, c)]

    while (r, c) != (0, 0):
        lr, lc = r, c - 1
        ur, uc = r - 1, c

        if 0 <= lr < H and 0 <= lc < W:
            l_val = dp[lr][lc]
        else:
            l_val = 987987987

        if 0 <= ur < H and 0 <= uc < W:
            u_val = dp[ur][uc]
        else:
            u_val = 987987987

        if u_val <= l_val:
            r, c = ur, uc
        else:
            r, c = lr, lc

        path.append((r, c))

    return path[::-1]


dp = [[987654321] * W for _ in range(H)]
visit = [[0] * W for _ in range(H)]

ans = getDP()
path = findPath()

print(ans)
for y, x in path:
    print('{},{}'.format(y, x))
