import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
tree = {}

for _ in range(N):
    v, l, r = map(str, input().split())
    tree[v] = (l, r)


def pre_order(alpha):
    if alpha == "." or tree.get(alpha, 0) == 0:
        return

    print(alpha, end="")
    pre_order(tree[alpha][0])
    pre_order(tree[alpha][1])


def in_order(alpha):
    if alpha == "." or tree.get(alpha, 0) == 0:
        return

    in_order(tree[alpha][0])
    print(alpha, end="")
    in_order(tree[alpha][1])


def post_order(alpha):
    if alpha == "." or tree.get(alpha, 0) == 0:
        return

    post_order(tree[alpha][0])
    post_order(tree[alpha][1])
    print(alpha, end="")


pre_order("A")
print()
in_order("A")
print()
post_order("A")
