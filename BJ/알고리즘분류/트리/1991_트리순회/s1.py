import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
tree = [""] * (2**N+1)
tree_idx = {}


def add_tree(node, value):
    if tree[node] != "":
        return
    tree[node] = value
    tree_idx[value] = node


def set_tree():
    for i in range(1, N+1):
        v, l, r = map(str, input().split())

        if tree_idx.get(v, 0):
            i = tree_idx[v]
        else:
            add_tree(i, v)

        if l != ".":
            add_tree(i * 2, l)
        if r != ".":
            add_tree(i * 2 + 1, r)


def pre_order(node):
    if node > 2**N + 1 or tree[node] == "":
        return

    print(tree[node], end="")
    pre_order(node*2)
    pre_order(node*2 + 1)


def in_order(node):
    if node > 2 ** N + 1 or tree[node] == "":
        return

    in_order(node * 2)
    print(tree[node], end="")
    in_order(node * 2 + 1)


def post_order(node):
    if node > 2 ** N + 1 or tree[node] == "":
        return

    post_order(node * 2)
    post_order(node * 2 + 1)
    print(tree[node], end="")


set_tree()
pre_order(1)
print()
in_order(1)
print()
post_order(1)