import sys

sys.setrecursionlimit(1000000)
sys.stdin = open('input.txt')
input = sys.stdin.readline


class Tree:
    def __init__(self):
        self.tree = {}

    def set_root(self, node):
        self.tree[node] = (0, 0)

    def set_left(self, node, left):
        self.tree[node] = (left, self.tree[node][1])

    def set_right(self, node, right):
        self.tree[node] = (self.tree[node][0], right)

    def get_left(self, node):
        return self.tree[node][0]

    def get_right(self, node):
        return self.tree[node][1]

    def get_tree(self):
        return self.tree

    def have_child(self, node):
        if self.tree.get(node, -1) == -1:
            return False
        else:
            return True


tree = Tree()


def set_tree(preo, ino):
    if len(preo) == 1:
        return preo[0]
    elif len(preo) == 0:
        return 0

    root = preo[0]
    tree.set_root(root)

    root_idx = ino.index(root)
    left = ino[:root_idx]
    right = ino[root_idx+1:]

    left_c = set_tree(preo[1: len(left) + 1], left)
    right_c = set_tree(preo[len(left) + 1:], right)

    tree.set_left(root, left_c)
    tree.set_right(root, right_c)

    return root


def post_order(p):
    if tree.have_child(p):
        post_order(tree.get_left(p))
        post_order(tree.get_right(p))

    if p:
        print(p, end=" ")


T = int(input())
for _ in range(T):
    N = int(input())
    pre_order = list(map(int, input().split()))
    in_order = list(map(int, input().split()))
    set_tree(pre_order, in_order)
    post_order(pre_order[0])
    print()

