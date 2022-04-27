import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

n, T = map(int, input().split())

coordinate = [tuple(map(int, input().split())) for _ in range(n)]
visited = {}


def is_available(x, y, nxt_x, nxt_y):
    if abs(nxt_x - x) <= 2 and abs(nxt_y - y) <= 2:
        return True
    return False


def bfs(k):
    que = [(0, 0, 0)]
    while que:
        x, y, cnt = que.pop(0)

        if y == T:
            return True

        if cnt >= k:
            return False

        if cnt > visited.get((x, y), 999):
            continue
        visited[(x, y)] = cnt

        for nxt_x, nxt_y in coordinate:
            if not is_available(x, y, nxt_x, nxt_y):
                continue

            que.append((nxt_x, nxt_y, cnt + 1))


def solution(left, right):
    global ans
    if right <= left:
        return ans

    m = (left + right) // 2

    if bfs(m):
        ans = m
        return solution(left, m)
    else:
        return solution(m+1, right)


ans = -1
print(solution(T//2, n))