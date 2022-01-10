import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
tree = {p: [-1, -1, 0] for p in range(1, N+1)}
result = {}

for _ in range(N):
    p, l, r = map(int, input().split())
    tree[p][0] = l
    tree[p][1] = r
    if l > 0: tree[l][2] = p
    if r > 0: tree[r][2] = p

col = 1


def get_root():
    node = 1
    while tree[node][2] != 0:
        node = tree[node][2]
    return node


def in_order(node, level):
    global col
    if node == -1:
        return

    in_order(tree[node][0], level + 1)
    result[level] = result.get(level, []) + [col]
    col += 1
    in_order(tree[node][1], level + 1)


ans = []

root = get_root()
in_order(root, 1)

for level, cols in result.items():
    val = max(cols) - min(cols) + 1
    ans.append((val, level))

ans.sort(key=lambda x: (-x[0], x[1]))

print(*ans[0][::-1])
