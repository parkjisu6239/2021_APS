import sys

sys.stdin = open('input.txt')
lines = sys.stdin.readlines()

trees = {}
tc = 1


def is_tree(tree):
    node = set()
    p = {}
    for u, v in tree:
        if p.get(v, 0): # 부모가 하나보다 많으면 트리가 아니다.
            return False
        p[v] = u
        node.add(u)
        node.add(v)

    if len(tree) != len(node) - 1:
        return False # 노드 - 1 == 간선 성립하지 않으면 트리가 아니다.

    root = 0
    for v in list(node):
        if p.get(v, 0) == 0:
            root += 1

    if root == 1:
        return True # 루트가 하나면 트리다
    else:
        return False # 루트가 하나가 아니면, 트리가 아니다.


for line in lines:
    for pair in line.split("  "):
        if len(pair) > 2:
            u, v = map(int, pair.split())
            if u > 0 and v > 0:
                trees[tc] = trees.get(tc, []) + [(u, v)]
            elif u == v == 0:
                if trees.get(tc, 0) == 0:
                    trees[tc] = []
                tc += 1


for tc, tree in trees.items():
    if len(tree) == 0 or is_tree(tree): # 빈배열도 트리다.
        print("Case " + str(tc) + " is a tree.")
    else:
        print("Case " + str(tc) + " is not a tree.")



